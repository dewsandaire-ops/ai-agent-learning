import json
import os


NOTES_FILE = "agent_memory.json"


def _load_notes():
    if not os.path.exists(NOTES_FILE):
        return []

    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def _save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2, ensure_ascii=False)


def save_note(note):
    """Save a note."""
    notes = _load_notes()
    notes.append(note)
    _save_notes(notes)

    return f"Note saved: {note}"


def read_notes():
    """Read all saved notes."""
    notes = _load_notes()

    if not notes:
        return "There are no saved notes."

    return "\n".join(
        f"{index + 1}. {note}"
        for index, note in enumerate(notes)
    )


def delete_note(note):
    """Delete a matching saved note."""
    notes = _load_notes()

    if note not in notes:
        return f"Note not found: {note}"

    notes.remove(note)
    _save_notes(notes)

    return f"Note deleted: {note}"
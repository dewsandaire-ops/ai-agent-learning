import os


NOTES_FILE = "agent_notes.txt"


def save_note(note):
    try:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(note.strip() + "\n")

        return f"Note saved successfully: {note}"

    except OSError as error:
        return f"Could not save note: {error}"


def read_notes():
    try:
        if not os.path.exists(NOTES_FILE):
            return "There are no saved notes yet."

        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.read().strip()

        if not notes:
            return "There are no saved notes yet."

        return notes

    except OSError as error:
        return f"Could not read notes: {error}"


def delete_note(note):
    try:
        if not os.path.exists(NOTES_FILE):
            return "There are no saved notes."

        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.readlines()

        target = note.strip().lower()

        remaining_notes = [
            saved_note
            for saved_note in notes
            if target not in saved_note.strip().lower()
        ]

        if len(remaining_notes) == len(notes):
            return "I could not find that note."

        with open(NOTES_FILE, "w", encoding="utf-8") as file:
            file.writelines(remaining_notes)

        return f"Note deleted successfully: {note}"

    except OSError as error:
        return f"Could not delete note: {error}"
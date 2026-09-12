import os

from dotenv import load_dotenv

try:
    from brain import ask_ai, create_client  # pyright: ignore[reportMissingImports]
except ImportError:  # pragma: no cover - supports both direct execution and package imports
    from .brain import ask_ai, create_client  # pyright: ignore[reportMissingImports]


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. "
        "Please check your .env file."
    )


# ============================================================
# CREATE OPENAI CLIENT
# ============================================================

client = create_client(OPENAI_API_KEY)


# ============================================================
# FOUR AI ASSISTANTS
# ============================================================

ASSISTANTS = {
    "1": {
        "name": "Venus",
        "business": "Verified Agents and Homes",
        "key": "venus",
    },
    "2": {
        "name": "Dews",
        "business": "Dews and Aire Nig. Ltd.",
        "key": "dews",
    },
    "3": {
        "name": "Jahz",
        "business": "JAHZ Empire Hotel & Suites",
        "key": "jahz",
    },
    "4": {
        "name": "You",
        "business": "Lagos MoveSmart",
        "key": "movesmart",
    },
}


# ============================================================
# DISPLAY MAIN MENU
# ============================================================

def show_menu():
    print()
    print("================================================")
    print("              MY AI AGENT SYSTEM")
    print("================================================")
    print()
    print("Choose the AI assistant you want to use:")
    print()
    print("1. Venus  - Verified Agents and Homes")
    print("2. Dews   - Dews and Aire Nig. Ltd.")
    print("3. Jahz   - JAHZ Empire Hotel & Suites")
    print("4. You    - Lagos MoveSmart")
    print()
    print("Type 'exit' to close the program.")
    print()


# ============================================================
# RUN ONE ASSISTANT
# ============================================================

def run_assistant(assistant):
    assistant_name = assistant["name"]
    business_name = assistant["business"]
    assistant_key = assistant["key"]

    print()
    print("================================================")
    print(f"{assistant_name} AI")
    print(f"{business_name}")
    print("================================================")
    print()
    print("Assistant is ready.")
    print("Type 'back' to return to the main menu.")
    print("Type 'exit' to close the program.")
    print()

    while True:
        try:
            message = input("You: ").strip()

            if not message:
                continue

            if message.lower() == "back":
                print()
                print("Returning to the main menu...")
                return

            if message.lower() in {"exit", "quit"}:
                print()
                print("AI Agent stopped.")
                raise SystemExit

            answer = ask_ai(
                client,
                message,
                assistant=assistant_key,
            )

            print()
            print(f"{assistant_name}:", answer)
            print()

        except KeyboardInterrupt:
            print()
            print()
            print("Returning to the main menu...")
            return

        except SystemExit:
            raise

        except (TypeError, ValueError, RuntimeError, OSError) as error:
            print()
            print("ERROR:", error)
            print()


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    while True:

        show_menu()

        choice = input("Choose 1, 2, 3, or 4: ").strip()

        if choice.lower() in {"exit", "quit"}:
            print()
            print("AI Agent stopped.")
            break

        if choice not in ASSISTANTS:
            print()
            print("Invalid choice.")
            print("Please choose 1, 2, 3, or 4.")
            continue

        selected_assistant = ASSISTANTS[choice]

        run_assistant(selected_assistant)


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()
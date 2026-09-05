import os

from agent.brain import ask_ai, create_client


def main():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("OpenAI API key is not set.")
        print("Please set the OPENAI_API_KEY environment variable.")
        return

    client = create_client(api_key)

    print("===================================")
    print("        MY AI AGENT")
    print("===================================")
    print("AI Agent is ready.")
    print("Type 'exit' to stop.")
    print()

    while True:
        try:
            user_message = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_message:
            continue

        if user_message.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        response = ask_ai(
            client,
            user_message,
        )

        print(f"\nAI: {response}")
        print()


if __name__ == "__main__":
    main()
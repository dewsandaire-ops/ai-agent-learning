from agent.brain import ask_ai


def main():
    import os

    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("OPENAI_API_KEY is not set.")
        print("Please set your OpenAI API key before running the agent.")
        return

    client = OpenAI(api_key=api_key)

    print("================================")
    print("       My AI Agent")
    print("================================")
    print("Type 'exit' to stop the agent.\n")

    while True:
        message = input("You: ")

        if message.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_ai(client, message)

        print(f"\nAI: {answer}\n")


if __name__ == "__main__":
    main()
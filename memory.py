import json
import os


MEMORY_FILE = "memory.json"

MAX_MESSAGES = 20


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        if isinstance(data, list):
            return data[-MAX_MESSAGES:]

        if isinstance(data, dict):

            conversation = data.get("conversation")

            if isinstance(conversation, list):
                return conversation[-MAX_MESSAGES:]

        return []

    except (
        json.JSONDecodeError,
        OSError
    ):

        return []


def save_memory(conversation):

    try:

        recent_conversation = conversation[-MAX_MESSAGES:]

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                recent_conversation,
                file,
                indent=4,
                ensure_ascii=False
            )

    except OSError as error:

        print(f"Memory error: {error}")
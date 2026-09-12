import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from brain import ask_ai, create_client


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
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Verified Agents and Homes AI",
    description="AI system for four business assistants.",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# CHAT REQUEST
# ============================================================

class ChatRequest(BaseModel):
    assistant: str = "venus"
    message: str


# ============================================================
# HOME / STATUS
# ============================================================

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "AI Agent system is running.",
        "assistants": [
            "venus",
            "dews",
            "jahz",
            "movesmart",
        ],
    }


# ============================================================
# CHAT ENDPOINT
# ============================================================

@app.post("/chat")
def chat(request: ChatRequest):

    assistant = str(
        request.assistant or "venus"
    ).strip().lower()

    message = str(
        request.message or ""
    ).strip()

    # Allow "you" as the Lagos MoveSmart assistant.
    if assistant == "you":
        assistant = "movesmart"

    # Prevent empty messages.
    if not message:
        return {
            "answer": "Please enter a message."
        }

    # Allow only the four assistants.
    allowed_assistants = {
        "venus",
        "dews",
        "jahz",
        "movesmart",
    }

    if assistant not in allowed_assistants:
        return {
            "answer": (
                "The selected AI assistant is not available."
            )
        }

    try:

        answer = ask_ai(
            client,
            message,
            assistant=assistant,
        )

        return {
            "assistant": assistant,
            "answer": answer,
        }

    except Exception as error:  # noqa: BLE001

        print("CHAT ERROR:", error)

        return {
            "answer": (
                "I'm sorry, I ran into a problem "
                "while processing your request."
            )
        }

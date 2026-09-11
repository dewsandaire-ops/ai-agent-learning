# ruff: noqa: I001
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel

from agent.brain import ask_ai


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set.")

client = OpenAI(api_key=api_key)


# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="Business AI Assistant System",
    version="1.0.0",
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
# WEBSITE REQUEST MODEL
# ============================================================

class ChatRequest(BaseModel):
    message: str
    assistant: str | None = None


# ============================================================
# WEBSITE ASSISTANT ROUTING
# ============================================================

WEBSITE_ASSISTANTS = {
    "verifiedagentsandhomes.com": "venus",
    "www.verifiedagentsandhomes.com": "venus",

    "dewsandaire.com": "dews",
    "www.dewsandaire.com": "dews",

    "jahzempiresuites.com": "jahz",
    "www.jahzempiresuites.com": "jahz",

    "lagosmovesmart.com": "movesmart",
    "www.lagosmovesmart.com": "movesmart",
}


def get_assistant_from_website(request: Request):
    """
    Identify the correct assistant from the website domain
    that sent the chatbot request.
    """

    origin = request.headers.get("origin", "")
    referer = request.headers.get("referer", "")

    website_source = origin or referer

    if not website_source:
        return None

    website_source = (
        website_source
        .lower()
        .replace("https://", "")
        .replace("http://", "")
        .split("/")[0]
        .split(":")[0]
    )

    return WEBSITE_ASSISTANTS.get(website_source)


def normalize_assistant(assistant):
    """
    Normalize assistant names and display names.
    """

    if not assistant:
        return None

    assistant = str(assistant).strip().lower()

    if assistant == "you":
        return "movesmart"

    if assistant in {
        "venus",
        "dews",
        "jahz",
        "movesmart",
    }:
        return assistant

    return None


# ============================================================
# HOME ROUTE
# ============================================================

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Business AI Assistant System is running.",
    }


# ============================================================
# HEALTH CHECK ROUTE
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Business AI Assistant System",
    }


# ============================================================
# CHAT ROUTE
# ============================================================

@app.post("/chat")
def chat(request_data: ChatRequest, request: Request):

    # --------------------------------------------------------
    # First priority:
    # identify the assistant from the website domain.
    # --------------------------------------------------------

    website_assistant = get_assistant_from_website(request)

    # --------------------------------------------------------
    # Second priority:
    # use the assistant sent directly by the website/API.
    # --------------------------------------------------------

    requested_assistant = normalize_assistant(
        request_data.assistant
    )

    # --------------------------------------------------------
    # Select the correct assistant.
    # --------------------------------------------------------

    if website_assistant:
        selected_assistant = website_assistant

    elif requested_assistant:
        selected_assistant = requested_assistant

    else:
        selected_assistant = "venus"

    # --------------------------------------------------------
    # Send the message to the selected assistant.
    # --------------------------------------------------------

    answer = ask_ai(
        client,
        request_data.message,
        selected_assistant,
    )

    # --------------------------------------------------------
    # Return the answer and selected assistant.
    # --------------------------------------------------------

    return {
        "answer": answer,
        "assistant": selected_assistant,
    }

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
    title="Business AI Assistant System"
)


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
# WEBSITE DOMAIN ROUTING
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
    Identify the correct assistant from the website that
    sent the chatbot request.
    """

    origin = request.headers.get("origin", "")
    referer = request.headers.get("referer", "")

    website_source = origin or referer

    website_source = (
        website_source
        .lower()
        .replace("https://", "")
        .replace("http://", "")
        .split("/")[0]
        .split(":")[0]
    )

    return WEBSITE_ASSISTANTS.get(website_source)


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
# CHAT ROUTE
# ============================================================

@app.post("/chat")
def chat(request_data: ChatRequest, request: Request):

    # First identify the assistant from the website domain.
    website_assistant = get_assistant_from_website(request)

    # If the website is recognized, trust the website routing.
    # This prevents a website from accidentally using Venus.
    if website_assistant:
        selected_assistant = website_assistant

    # This supports direct API testing when no website origin exists.
    elif request_data.assistant:
        selected_assistant = request_data.assistant.strip().lower()

    # Safe fallback for direct requests only.
    else:
        selected_assistant = "venus"

    answer = ask_ai(
        client,
        request_data.message,
        selected_assistant,
    )

    return {
        "answer": answer,
        "assistant": selected_assistant,
    }
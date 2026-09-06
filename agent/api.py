import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel

from agent.brain import ask_ai


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set.")

client = OpenAI(api_key=api_key)

app = FastAPI(title="Business AI Assistant System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    assistant: str = "venus"


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Business AI Assistant System is running."
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_ai(
        client,
        request.message,
        request.assistant,
    )

    return {
        "answer": answer
    }
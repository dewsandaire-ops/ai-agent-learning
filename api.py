# ruff: noqa: I001

import json
import os
import urllib.error
import urllib.request

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
# WHATSAPP ENVIRONMENT
# ============================================================

WHATSAPP_VERIFY_TOKEN = os.getenv(
    "WHATSAPP_VERIFY_TOKEN"
)

WHATSAPP_ACCESS_TOKEN = os.getenv(
    "WHATSAPP_ACCESS_TOKEN"
)

WHATSAPP_PHONE_NUMBER_ID = os.getenv(
    "WHATSAPP_PHONE_NUMBER_ID"
)

# The WhatsApp number initially uses Venus.
# We can later add a menu so customers can choose
# between Venus, Dews, Jahz, and MoveSmart.
WHATSAPP_ASSISTANT = os.getenv(
    "WHATSAPP_ASSISTANT",
    "venus",
)


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

    return WEBSITE_ASSISTANTS.get(
        website_source
    )


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
        "assistants": [
            "venus",
            "dews",
            "jahz",
            "movesmart",
        ],
        "whatsapp_webhook": "/webhook",
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
# WEBSITE CHAT ROUTE
# ============================================================

@app.post("/chat")
def chat(
    request_data: ChatRequest,
    request: Request,
):

    # --------------------------------------------------------
    # First priority:
    # identify the assistant from the website domain.
    # --------------------------------------------------------

    website_assistant = get_assistant_from_website(
        request
    )

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


# ============================================================
# WHATSAPP WEBHOOK VERIFICATION
# ============================================================

@app.get("/webhook")
async def verify_whatsapp_webhook(
    request: Request,
):
    """
    Meta uses this GET request to verify the webhook.
    """

    params = request.query_params

    mode = params.get("hub.mode")

    verify_token = params.get(
        "hub.verify_token"
    )

    challenge = params.get(
        "hub.challenge"
    )

    if (
        mode == "subscribe"
        and verify_token
        and challenge
        and WHATSAPP_VERIFY_TOKEN
        and verify_token == WHATSAPP_VERIFY_TOKEN
    ):
        return int(challenge)

    return {
        "status": "verification failed"
    }


# ============================================================
# SEND MESSAGE TO WHATSAPP
# ============================================================

def send_whatsapp_message(
    recipient_phone,
    message,
):
    """
    Send an outgoing WhatsApp text message through
    the Meta WhatsApp Cloud API.
    """

    if not WHATSAPP_ACCESS_TOKEN:
        print(
            "WHATSAPP_ACCESS_TOKEN is not configured."
        )
        return False

    if not WHATSAPP_PHONE_NUMBER_ID:
        print(
            "WHATSAPP_PHONE_NUMBER_ID is not configured."
        )
        return False

    url = (
        "https://graph.facebook.com/v26.0/"
        f"{WHATSAPP_PHONE_NUMBER_ID}/messages"
    )

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient_phone,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": message,
        },
    }

    data = json.dumps(payload).encode(
        "utf-8"
    )

    request = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Authorization": (
                "Bearer "
                f"{WHATSAPP_ACCESS_TOKEN}"
            ),
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=30,
        ) as response:

            response_body = response.read().decode(
                "utf-8"
            )

            print(
                "WhatsApp send response:",
                response_body,
            )

            return True

    except urllib.error.HTTPError as error:

        error_body = error.read().decode(
            "utf-8",
            errors="replace",
        )

        print(
            "WhatsApp API error:",
            error.code,
            error_body,
        )

        return False

    except Exception as error:

        print(
            "WhatsApp send error:",
            error,
        )

        return False


# ============================================================
# EXTRACT WHATSAPP TEXT MESSAGE
# ============================================================

def extract_whatsapp_message(data):
    """
    Extract the sender's WhatsApp number and text message
    from a Meta webhook payload.

    Returns:

        (sender_phone, message_text)

    or:

        (None, None)
    """

    try:
        entries = data.get(
            "entry",
            [],
        )

        for entry in entries:

            changes = entry.get(
                "changes",
                [],
            )

            for change in changes:

                value = change.get(
                    "value",
                    {},
                )

                messages = value.get(
                    "messages",
                    [],
                )

                if not messages:
                    continue

                message = messages[0]

                sender_phone = message.get(
                    "from"
                )

                message_type = message.get(
                    "type"
                )

                # ------------------------------------------------
                # We currently respond only to text messages.
                # ------------------------------------------------

                if message_type == "text":

                    text_data = message.get(
                        "text",
                        {},
                    )

                    message_text = text_data.get(
                        "body"
                    )

                    if (
                        sender_phone
                        and message_text
                    ):
                        return (
                            sender_phone,
                            message_text,
                        )

                # ------------------------------------------------
                # If the user sends an unsupported message type.
                # ------------------------------------------------

                if sender_phone:
                    return (
                        sender_phone,
                        None,
                    )

    except Exception as error:

        print(
            "WhatsApp message extraction error:",
            error,
        )

    return (
        None,
        None,
    )


# ============================================================
# WHATSAPP WEBHOOK RECEIVER
# ============================================================

@app.post("/webhook")
async def whatsapp_webhook(
    request: Request,
):
    """
    Receive incoming WhatsApp webhook events.

    The flow is:

    WhatsApp
        ↓
    Meta
        ↓
    /webhook
        ↓
    extract message
        ↓
    brain.py
        ↓
    selected AI assistant
        ↓
    Meta WhatsApp API
        ↓
    customer receives reply
    """

    try:
        data = await request.json()

    except Exception:

        return {
            "status": "invalid json"
        }

    print()
    print(
        "========================================"
    )
    print(
        "WHATSAPP WEBHOOK RECEIVED"
    )
    print(
        "========================================"
    )
    print(data)
    print()

    # --------------------------------------------------------
    # Extract incoming WhatsApp message.
    # --------------------------------------------------------

    sender_phone, message_text = (
        extract_whatsapp_message(data)
    )

    # --------------------------------------------------------
    # Ignore webhook events that are not messages.
    # --------------------------------------------------------

    if not sender_phone:

        return {
            "status": "received",
            "message": "No incoming message found.",
        }

    # --------------------------------------------------------
    # Handle unsupported message types.
    # --------------------------------------------------------

    if not message_text:

        print(
            "Unsupported WhatsApp message type."
        )

        send_whatsapp_message(
            sender_phone,
            (
                "Sorry, I can currently "
                "understand text messages only."
            ),
        )

        return {
            "status": "received",
            "message": (
                "Unsupported message type."
            ),
        }

    print(
        "WhatsApp sender:",
        sender_phone,
    )

    print(
        "WhatsApp message:",
        message_text,
    )

    # --------------------------------------------------------
    # Select the WhatsApp assistant.
    # --------------------------------------------------------

    selected_assistant = normalize_assistant(
        WHATSAPP_ASSISTANT
    )

    if not selected_assistant:
        selected_assistant = "venus"

    print(
        "WhatsApp assistant:",
        selected_assistant,
    )

    # --------------------------------------------------------
    # Send the WhatsApp message to the AI.
    # --------------------------------------------------------

    try:

        answer = ask_ai(
            client,
            message_text,
            selected_assistant,
        )

    except Exception as error:

        print(
            "WhatsApp AI error:",
            error,
        )

        answer = (
            "I'm sorry, I encountered a problem "
            "while processing your message. "
            "Please try again."
        )

    print(
        "AI answer:",
        answer,
    )

    # --------------------------------------------------------
    # Send AI answer back to WhatsApp.
    # --------------------------------------------------------

    sent = send_whatsapp_message(
        sender_phone,
        answer,
    )

    if sent:

        print(
            "WhatsApp reply sent successfully."
        )

    else:

        print(
            "WhatsApp reply could not be sent."
        )

    return {
        "status": "received",
        "assistant": selected_assistant,
        "reply_sent": sent,
    }

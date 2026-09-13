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


# ============================================================
# WHATSAPP BUSINESS NUMBERS
# ============================================================
#
# Each WhatsApp number belongs to ONE assistant only.
#
# Dews & Aire:
# 08024981447 -> dews
#
# JAHZ Empire:
# 07062754478 -> jahz
# 08069519327 -> jahz
#
# Verified Agents & Homes:
# 09062029300 -> venus
#
# Lagos MoveSmart:
# 09062028300 -> movesmart
#
# No customer menu is used.
# The WhatsApp number automatically determines
# which assistant answers.
# ============================================================

WHATSAPP_NUMBER_ASSISTANTS = {
    "2348024981447": "dews",

    "2347062754478": "jahz",
    "2348069519327": "jahz",

    "2349062029300": "venus",

    "2349062028300": "movesmart",
}


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
# NORMALIZE WHATSAPP PHONE NUMBER
# ============================================================

def normalize_phone_number(phone_number):
    """
    Convert Nigerian WhatsApp numbers into one consistent format.

    Example:

        08024981447
        +2348024981447
        2348024981447

    all become:

        2348024981447
    """

    if not phone_number:
        return None

    phone_number = str(phone_number).strip()

    # Remove common formatting characters.
    phone_number = (
        phone_number
        .replace("+", "")
        .replace(" ", "")
        .replace("-", "")
        .replace("(", "")
        .replace(")", "")
    )

    # Convert Nigerian local format.
    if phone_number.startswith("0"):
        phone_number = (
            "234" + phone_number[1:]
        )

    return phone_number


# ============================================================
# GET ASSISTANT FROM WHATSAPP BUSINESS NUMBER
# ============================================================

def get_whatsapp_assistant(
    display_phone_number,
):
    """
    Select the assistant based ONLY on the WhatsApp
    business number that received the message.

    This keeps all four businesses completely separate.
    """

    normalized_number = normalize_phone_number(
        display_phone_number
    )

    if not normalized_number:
        return None

    return WHATSAPP_NUMBER_ASSISTANTS.get(
        normalized_number
    )


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
    phone_number_id,
):
    """
    Send an outgoing WhatsApp text message.

    phone_number_id is the ID of the WhatsApp business
    number that received the customer's message.

    This ensures the reply goes back through the SAME
    WhatsApp business number.
    """

    if not WHATSAPP_ACCESS_TOKEN:
        print(
            "WHATSAPP_ACCESS_TOKEN is not configured."
        )
        return False

    if not phone_number_id:
        print(
            "WhatsApp phone number ID is missing."
        )
        return False

    url = (
        "https://graph.facebook.com/v26.0/"
        f"{phone_number_id}/messages"
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

            response_body = (
                response.read()
                .decode("utf-8")
            )

            print(
                "WhatsApp send response:",
                response_body,
            )

            return True

    except urllib.error.HTTPError as error:

        error_body = (
            error.read()
            .decode(
                "utf-8",
                errors="replace",
            )
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
# EXTRACT WHATSAPP MESSAGE
# ============================================================

def extract_whatsapp_message(data):
    """
    Extract:

    1. Customer's WhatsApp number
    2. Customer's message
    3. WhatsApp business phone number ID
    4. WhatsApp business display phone number

    from the Meta webhook payload.

    Returns:

        (
            sender_phone,
            message_text,
            phone_number_id,
            display_phone_number,
        )

    or:

        (None, None, None, None)
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

                metadata = value.get(
                    "metadata",
                    {},
                )

                phone_number_id = metadata.get(
                    "phone_number_id"
                )

                display_phone_number = (
                    metadata.get(
                        "display_phone_number"
                    )
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
                # Text message
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
                            phone_number_id,
                            display_phone_number,
                        )

                # ------------------------------------------------
                # Unsupported message type
                # ------------------------------------------------

                if sender_phone:

                    return (
                        sender_phone,
                        None,
                        phone_number_id,
                        display_phone_number,
                    )

    except Exception as error:

        print(
            "WhatsApp message extraction error:",
            error,
        )

    return (
        None,
        None,
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

    Each WhatsApp business number is connected
    to its own AI assistant.

    Dews number
        ↓
    Dews assistant

    JAHZ number
        ↓
    Jahz assistant

    Verified Agents number
        ↓
    Venus assistant

    Lagos MoveSmart number
        ↓
    MoveSmart assistant
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
    # Extract WhatsApp information.
    # --------------------------------------------------------

    (
        sender_phone,
        message_text,
        phone_number_id,
        display_phone_number,
    ) = extract_whatsapp_message(data)

    # --------------------------------------------------------
    # Ignore events that are not incoming messages.
    # --------------------------------------------------------

    if not sender_phone:

        return {
            "status": "received",
            "message": (
                "No incoming WhatsApp message found."
            ),
        }

    # --------------------------------------------------------
    # Make sure Meta supplied the business number.
    # --------------------------------------------------------

    if not display_phone_number:

        print(
            "WhatsApp business number was not found."
        )

        return {
            "status": "received",
            "message": (
                "WhatsApp business number "
                "could not be identified."
            ),
        }

    # --------------------------------------------------------
    # Select assistant based on the business number.
    # --------------------------------------------------------

    selected_assistant = (
        get_whatsapp_assistant(
            display_phone_number
        )
    )

    # --------------------------------------------------------
    # SECURITY:
    # Never guess an assistant if the WhatsApp number
    # is not registered in our business-number map.
    # --------------------------------------------------------

    if not selected_assistant:

        print(
            "Unknown WhatsApp business number:",
            display_phone_number,
        )

        return {
            "status": "ignored",
            "message": (
                "WhatsApp number is not registered "
                "with an assistant."
            ),
        }

    print(
        "WhatsApp business number:",
        display_phone_number,
    )

    print(
        "WhatsApp phone number ID:",
        phone_number_id,
    )

    print(
        "Customer WhatsApp number:",
        sender_phone,
    )

    print(
        "Selected assistant:",
        selected_assistant,
    )

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
            phone_number_id,
        )

        return {
            "status": "received",
            "message": (
                "Unsupported message type."
            ),
            "assistant": selected_assistant,
        }

    print(
        "WhatsApp message:",
        message_text,
    )

    # --------------------------------------------------------
    # Send the message ONLY to the selected assistant.
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
    # Send the AI answer back through the SAME
    # WhatsApp business number.
    # --------------------------------------------------------

    sent = send_whatsapp_message(
        sender_phone,
        answer,
        phone_number_id,
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
        "business_number": display_phone_number,
        "reply_sent": sent,
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
    phone_number_id,
):
    """
    Send an outgoing WhatsApp text message.

    phone_number_id is the ID of the WhatsApp business
    number that received the customer's message.

    This ensures the reply goes back through the SAME
    WhatsApp business number.
    """

    if not WHATSAPP_ACCESS_TOKEN:
        print(
            "WHATSAPP_ACCESS_TOKEN is not configured."
        )
        return False

    if not phone_number_id:
        print(
            "WhatsApp phone number ID is missing."
        )
        return False

    url = (
        "https://graph.facebook.com/v26.0/"
        f"{phone_number_id}/messages"
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

            response_body = (
                response.read()
                .decode("utf-8")
            )

            print(
                "WhatsApp send response:",
                response_body,
            )

            return True

    except urllib.error.HTTPError as error:

        error_body = (
            error.read()
            .decode(
                "utf-8",
                errors="replace",
            )
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
# EXTRACT WHATSAPP MESSAGE
# ============================================================

def extract_whatsapp_message(data):
    """
    Extract:

    1. Customer's WhatsApp number
    2. Customer's message
    3. WhatsApp business phone number ID
    4. WhatsApp business display phone number

    from the Meta webhook payload.

    Returns:

        (
            sender_phone,
            message_text,
            phone_number_id,
            display_phone_number,
        )

    or:

        (None, None, None, None)
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

                metadata = value.get(
                    "metadata",
                    {},
                )

                phone_number_id = metadata.get(
                    "phone_number_id"
                )

                display_phone_number = (
                    metadata.get(
                        "display_phone_number"
                    )
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
                # Text message
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
                            phone_number_id,
                            display_phone_number,
                        )

                # ------------------------------------------------
                # Unsupported message type
                # ------------------------------------------------

                if sender_phone:

                    return (
                        sender_phone,
                        None,
                        phone_number_id,
                        display_phone_number,
                    )

    except Exception as error:

        print(
            "WhatsApp message extraction error:",
            error,
        )

    return (
        None,
        None,
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

    Each WhatsApp business number is connected
    to its own AI assistant.

    Dews number
        ↓
    Dews assistant

    JAHZ number
        ↓
    Jahz assistant

    Verified Agents number
        ↓
    Venus assistant

    Lagos MoveSmart number
        ↓
    MoveSmart assistant
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
    # Extract WhatsApp information.
    # --------------------------------------------------------

    (
        sender_phone,
        message_text,
        phone_number_id,
        display_phone_number,
    ) = extract_whatsapp_message(data)

    # --------------------------------------------------------
    # Ignore events that are not incoming messages.
    # --------------------------------------------------------

    if not sender_phone:

        return {
            "status": "received",
            "message": (
                "No incoming WhatsApp message found."
            ),
        }

    # --------------------------------------------------------
    # Make sure Meta supplied the business number.
    # --------------------------------------------------------

    if not display_phone_number:

        print(
            "WhatsApp business number was not found."
        )

        return {
            "status": "received",
            "message": (
                "WhatsApp business number "
                "could not be identified."
            ),
        }

    # --------------------------------------------------------
    # Select assistant based on the business number.
    # --------------------------------------------------------

    selected_assistant = (
        get_whatsapp_assistant(
            display_phone_number
        )
    )

    # --------------------------------------------------------
    # SECURITY:
    # Never guess an assistant if the WhatsApp number
    # is not registered in our business-number map.
    # --------------------------------------------------------

    if not selected_assistant:

        print(
            "Unknown WhatsApp business number:",
            display_phone_number,
        )

        return {
            "status": "ignored",
            "message": (
                "WhatsApp number is not registered "
                "with an assistant."
            ),
        }

    print(
        "WhatsApp business number:",
        display_phone_number,
    )

    print(
        "WhatsApp phone number ID:",
        phone_number_id,
    )

    print(
        "Customer WhatsApp number:",
        sender_phone,
    )

    print(
        "Selected assistant:",
        selected_assistant,
    )

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
            phone_number_id,
        )

        return {
            "status": "received",
            "message": (
                "Unsupported message type."
            ),
            "assistant": selected_assistant,
        }

    print(
        "WhatsApp message:",
        message_text,
    )

    # --------------------------------------------------------
    # Send the message ONLY to the selected assistant.
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
    # Send the AI answer back through the SAME
    # WhatsApp business number.
    # --------------------------------------------------------

    sent = send_whatsapp_message(
        sender_phone,
        answer,
        phone_number_id,
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
        "business_number": display_phone_number,
        "reply_sent": sent,
    }
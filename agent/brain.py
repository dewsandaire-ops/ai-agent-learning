import json
from openai import OpenAI

from agent.tool_definitions import TOOLS_BY_ASSISTANT
from tools.tool_registry import get_tool


# ============================================================
# ASSISTANT INSTRUCTIONS
# ============================================================

ASSISTANT_INSTRUCTIONS = {
    "venus": """
You are Venus, the AI assistant for Verified Agents and Homes.

You must answer only for Verified Agents and Homes.

Never mention or provide information belonging to:
- Dews and Aire Nig. Ltd.
- JAHZ Empire Hotel & Suites
- Lagos MoveSmart

For questions about company information, property verification,
land and house documents, real-estate agents, short-let accommodation,
car hire, payment safety, FAQs, or business services, use the available
Verified Agents and Homes tools before answering.

Never invent information.

If the available Verified Agents and Homes information does not contain
the answer, say that the information is not currently available.

Do not ask the customer to provide a property ID unless the customer is
asking about a specific property and the tool genuinely requires it.
""",

    "dews": """
You are Dews, the AI assistant for Dews and Aire Nig. Ltd.

You must answer only for Dews and Aire Nig. Ltd.

Never mention or provide information belonging to:
- Verified Agents and Homes
- JAHZ Empire Hotel & Suites
- Lagos MoveSmart

For questions about Dews and Aire services, company information,
architecture, interior design, construction, renovation, property
management, short-let assistance, FAQs, recommendations, or enquiries,
use the available Dews and Aire tools before answering.

Never invent information.

If the available Dews and Aire information does not contain the answer,
say that the information is not currently available.

Do not list services belonging to the other businesses.
""",

    "jahz": """
You are Jahz, the AI assistant for JAHZ Empire Hotel & Suites.

You must answer only for JAHZ Empire Hotel & Suites.

Never mention or provide information belonging to:
- Verified Agents and Homes
- Dews and Aire Nig. Ltd.
- Lagos MoveSmart

For questions about the hotel, address, location, rooms, facilities,
services, prices, bookings, policies, FAQs, recommendations, or enquiries,
use the available JAHZ hotel tools before answering.

Business facts must come from the available JAHZ tools.

Never invent information.

If the available JAHZ information does not contain the answer,
say that the information is not currently available.
""",

    "movesmart": """
You are You, the AI assistant for Lagos MoveSmart.

You must answer only for Lagos MoveSmart.

Never mention or provide information belonging to:
- Verified Agents and Homes
- Dews and Aire Nig. Ltd.
- JAHZ Empire Hotel & Suites

For questions about Lagos transport safety, report categories,
reporting procedures, FAQs, emergency guidance, evidence, protected
information, rewards, follow-ups, or reports, use the available
Lagos MoveSmart tools before answering.

Never invent information.

If the available Lagos MoveSmart information does not contain the answer,
say that the information is not currently available.
""",
}


# ============================================================
# OPENAI CLIENT
# ============================================================

def create_client(api_key):
    return OpenAI(api_key=api_key)


# ============================================================
# TOOL EXECUTION
# ============================================================

def run_tool(tool_name, arguments):
    tool = get_tool(tool_name)

    if tool is None:
        return f"Tool '{tool_name}' was not found."

    try:
        return tool(**arguments)

    except (TypeError, ValueError) as error:
        return f"Tool error: {error}"

    except Exception as error:
        return f"Tool error: {error}"


# ============================================================
# MAIN AI FUNCTION
# ============================================================

def ask_ai(client, message, assistant="venus"):

    assistant = str(assistant or "venus").strip().lower()

    if assistant not in ASSISTANT_INSTRUCTIONS:
        assistant = "venus"

    instructions = ASSISTANT_INSTRUCTIONS[assistant]

    # Give each assistant only its own tools.
    assistant_tools = TOOLS_BY_ASSISTANT.get(assistant, [])

    allowed_tool_names = {
        tool["name"]
        for tool in assistant_tools
    }

    try:
        # ----------------------------------------------------
        # FIRST REQUEST
        # Force the model to use the selected business tools.
        # ----------------------------------------------------

        response = client.responses.create(
            model="gpt-5.6",
            instructions=instructions,
            tools=assistant_tools,
            tool_choice="required",
            input=message,
        )

        # ----------------------------------------------------
        # TOOL-CALL LOOP
        # ----------------------------------------------------

        while True:

            tool_outputs = []

            for item in response.output:

                if item.type != "function_call":
                    continue

                tool_name = item.name

                try:
                    arguments = json.loads(item.arguments)

                except (json.JSONDecodeError, TypeError):
                    result = (
                        "The tool arguments could not be understood."
                    )

                else:

                    if tool_name not in allowed_tool_names:
                        result = (
                            "This tool is not available to the "
                            "selected assistant."
                        )

                    else:
                        result = run_tool(
                            tool_name,
                            arguments,
                        )

                tool_outputs.append(
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(result),
                    }
                )

            # Return the final answer when there are no more tools.
            if not tool_outputs:
                return response.output_text

            # Send the tool results back to OpenAI.
            response = client.responses.create(
                model="gpt-5.6",
                instructions=instructions,
                tools=assistant_tools,
                previous_response_id=response.id,
                input=tool_outputs,
            )

    except Exception as error:

        return (
            "I'm sorry, I ran into a problem while "
            f"processing your request: {error}"
        )
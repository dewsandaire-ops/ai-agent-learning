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

You must answer only questions related to Verified Agents and Homes.

Do not discuss businesses or services outside Verified Agents and Homes.

For questions about company information, property verification,
land and house documents, real-estate agents, short-let accommodation,
car hire, payment safety, FAQs, or business services, use the available
Verified Agents and Homes tools before answering.

Never invent information.

If the available Verified Agents and Homes information does not contain
the answer, say:

"The information is not currently available."

Do not ask the customer to provide a property ID unless the customer is
asking about a specific property and the tool genuinely requires it.

Always explain verification status accurately.

Never claim that a property, agent, document, owner, manager, or short-let
is verified unless the available tool confirms it.
""",

    "dews": """
You are Dews, the AI assistant for Dews and Aire Nig. Ltd.

You must answer only questions related to Dews and Aire Nig. Ltd.

Do not discuss businesses or services outside Dews and Aire Nig. Ltd.

For questions about architecture, interior design, construction,
renovation, project supervision, property management, short-let
assistance, company information, FAQs, recommendations, or enquiries,
use the available Dews and Aire tools before answering.

Never invent information.

If the available Dews and Aire information does not contain the answer,
say:

"The information is not currently available."

Do not list services that are not provided by the available Dews and Aire
tools.

Do not invent prices, addresses, availability, staff names, timelines,
or service details.
""",

    "jahz": """
You are Jahz, the AI assistant for JAHZ Empire Hotel & Suites.

You must answer only questions related to JAHZ Empire Hotel & Suites.

Do not discuss businesses or services outside JAHZ Empire Hotel & Suites.

For questions about the hotel, address, location, rooms, suites,
facilities, swimming pool, gym, events, bar, parties, membership,
flight booking enquiries, apartment accommodation, bookings, policies,
FAQs, recommendations, or enquiries, use the available JAHZ hotel tools
before answering.

Business facts must come from the available JAHZ tools.

Never invent information.

If the available JAHZ information does not contain the answer, say:

"The information is not currently available."

Do not invent room prices, room availability, booking confirmations,
opening hours, addresses, staff names, or other hotel information.

If the customer wants to make an enquiry, use the appropriate enquiry tool.
""",

    "movesmart": """
You are You, the AI assistant for Lagos MoveSmart.

You must answer only questions related to Lagos MoveSmart.

Do not discuss businesses or services outside Lagos MoveSmart.

For questions about Lagos transport safety, road problems, unsafe driving,
unsafe commercial vehicles, illegal pickup and drop-off, reporting
procedures, report categories, FAQs, emergency guidance, evidence,
protected information, rewards, follow-ups, or reports, use the available
Lagos MoveSmart tools before answering.

Never invent information.

If the available Lagos MoveSmart information does not contain the answer,
say:

"The information is not currently available."

A report is not automatically a verification or confirmation of an incident.

Do not claim that a government agency or authority has confirmed an incident
unless the available information actually says so.

If the user reports an emergency or immediate danger, advise the user to
contact the appropriate emergency or law-enforcement authority directly.

Do not expose protected information without proper authorization.
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

    except Exception as error:  # noqa: BLE001
        return f"Tool error: {error}"


# ============================================================
# MAIN AI FUNCTION
# ============================================================

def ask_ai(client, message, assistant="venus"):
    """
    Send a message to the correct business assistant.

    Each assistant receives only its own instructions and tools.
    """

    assistant = str(assistant or "venus").strip().lower()

    # Accept the display name "you" as Lagos MoveSmart.
    if assistant == "you":
        assistant = "movesmart"

    # Prevent unknown assistant names.
    if assistant not in ASSISTANT_INSTRUCTIONS:
        assistant = "venus"

    instructions = ASSISTANT_INSTRUCTIONS[assistant]

    # Give each assistant only its own tools.
    assistant_tools = TOOLS_BY_ASSISTANT.get(assistant, [])

    # Create a set of allowed tool names for extra protection.
    allowed_tool_names = {
        tool["name"]
        for tool in assistant_tools
    }

    try:
        # ====================================================
        # FIRST OPENAI REQUEST
        # ====================================================

        response = client.responses.create(
            model="gpt-5.6",
            instructions=instructions,
            tools=assistant_tools,
            tool_choice="required",
            input=message,
        )

        # ====================================================
        # TOOL-CALL LOOP
        # ====================================================

        while True:
            tool_outputs = []

            for item in response.output:

                # Ignore normal text and other response items.
                if item.type != "function_call":
                    continue

                tool_name = item.name

                print(f"AI selected tool: {tool_name}")

                # --------------------------------------------
                # Read the tool arguments
                # --------------------------------------------

                try:
                    arguments = json.loads(item.arguments)

                except (json.JSONDecodeError, TypeError):
                    result = "The tool arguments could not be understood."

                else:

                    # ----------------------------------------
                    # Security check:
                    # only use tools belonging to this assistant
                    # ----------------------------------------

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

                print("Tool result:", result)

                # --------------------------------------------
                # Return the tool result to OpenAI
                # --------------------------------------------

                tool_outputs.append(
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(result),
                    }
                )

            # =================================================
            # NO MORE TOOLS: RETURN THE FINAL ANSWER
            # =================================================

            if not tool_outputs:
                return response.output_text

            # =================================================
            # SEND TOOL RESULTS BACK TO OPENAI
            # =================================================

            response = client.responses.create(
                model="gpt-5.6",
                instructions=instructions,
                tools=assistant_tools,
                previous_response_id=response.id,
                input=tool_outputs,
            )

    except Exception as error:  # noqa: BLE001
        print("AI ERROR:", error)

        return (
            "I'm sorry, I ran into a problem while "
            f"processing your request: {error}"
        )
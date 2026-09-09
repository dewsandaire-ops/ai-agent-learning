import json

from openai import OpenAI

from agent.tool_definitions import TOOLS_BY_ASSISTANT
from tools.tool_registry import get_tool


# ============================================================
# ASSISTANT INSTRUCTIONS
# ============================================================

ASSISTANT_INSTRUCTIONS = {
    "venus": """
You are Venus, the customer-facing AI assistant for Verified Agents and Homes.

Only represent Verified Agents and Homes.

Do not provide information belonging to Dews and Aire Nig. Ltd.,
JAHZ Empire Hotel & Suites, or Lagos MoveSmart.

You can help customers with:
- company information
- company services
- property searches
- property verification
- house and land information
- property documents
- agent searches
- agent verification
- agent documents
- Lagos locations
- short-let information
- short-let verification
- FAQs
- payment safety guidance
- monthly verification information
- related Verified Agents and Homes services

Use the available Verified Agents and Homes tools whenever specific
business information is required.

Never invent property information, agent information, document information,
verification information, prices, addresses, availability, ownership,
or other business information.

Do not claim that something is verified unless the appropriate tool confirms it.

An Agent ID and a VAH Verification Number are different things.

The VAH Verification Number is a monthly verification number. Customers
should check the current verification status before transacting.
""",

    "dews": """
You are Dews, the customer-facing AI assistant for Dews and Aire Nig. Ltd.

Only represent Dews and Aire Nig. Ltd.

Do not provide information belonging to Verified Agents and Homes,
JAHZ Empire Hotel & Suites, or Lagos MoveSmart.

You can help customers with:
- company information
- architecture
- interior design
- construction
- project supervision
- project coordination
- property management
- short-let services
- Dews and Aire services
- service recommendations
- FAQs
- customer enquiries

Use the available Dews and Aire tools whenever specific business
information is required.

Never invent prices, availability, addresses, timelines, staff names,
services, or other business information.
""",

    "jahz": """
You are Jahz, the customer-facing AI assistant for JAHZ Empire Hotel & Suites.

Only represent JAHZ Empire Hotel & Suites.

Do not provide information belonging to Verified Agents and Homes,
Dews and Aire Nig. Ltd., or Lagos MoveSmart.

You can help customers with:
- hotel rooms and suites
- room booking enquiries
- hotel services
- events
- bar and parties
- swimming pool
- swimming training
- gym
- gym instructors
- hotel membership
- Air Peace flight booking enquiries
- apartment and short-let accommodation
- hotel FAQs

Use the available JAHZ hotel tools whenever specific hotel information
is required.

For questions about hotel location, address, rooms, prices, facilities,
policies, booking, check-in, check-out, or similar hotel information,
use the appropriate JAHZ FAQ tools.

Never invent room prices, availability, booking confirmations,
opening hours, addresses, staff names, or other hotel information.
""",

    "movesmart": """
You are You, the customer-facing AI assistant for Lagos MoveSmart.

Only represent Lagos MoveSmart.

Do not provide information belonging to Verified Agents and Homes,
Dews and Aire Nig. Ltd., or JAHZ Empire Hotel & Suites.

You can help customers with:
- road and traffic problems
- unsafe driving
- unsafe commercial vehicles
- illegal pickup or drop-off
- environmental and waste problems
- drainage and flooding
- streetlights
- traffic signals
- public infrastructure
- illegal or unsafe structures
- public safety
- crime and security
- other public problems
- incident reporting
- report status
- evidence requests
- protected information requests
- follow-ups
- FAQs
- rewards

Use the available Lagos MoveSmart tools whenever specific information
is required.

A report is a report of a problem. A report is not automatically
verification or confirmation.

Do not claim that an authority has confirmed an incident unless the
available information explicitly confirms it.

For emergencies or immediate danger, advise the customer to contact
the appropriate emergency or law-enforcement authority directly.

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

    except Exception as error:
        return f"Tool error: {error}"


# ============================================================
# MAIN AI FUNCTION
# ============================================================

def ask_ai(client, message, assistant="venus"):

    # Make sure assistant is always a clean string.
    assistant = str(assistant or "venus").strip().lower()

    # If an unknown assistant is supplied, safely use Venus.
    if assistant not in ASSISTANT_INSTRUCTIONS:
        assistant = "venus"

    # Get the correct instructions.
    instructions = ASSISTANT_INSTRUCTIONS[assistant]

    # Get ONLY the tools belonging to this assistant.
    assistant_tools = TOOLS_BY_ASSISTANT.get(assistant, [])

    # Create a list of tool names this assistant is allowed to use.
    allowed_tool_names = {
        tool["name"]
        for tool in assistant_tools
    }

    try:

        # --------------------------------------------------------
        # FIRST OPENAI REQUEST
        # --------------------------------------------------------

        response = client.responses.create(
            model="gpt-5.6",
            instructions=instructions,
            tools=assistant_tools,
            input=message,
        )

        # --------------------------------------------------------
        # TOOL LOOP
        # --------------------------------------------------------

        while True:

            tool_outputs = []

            for item in response.output:

                # Ignore normal text output.
                if item.type != "function_call":
                    continue

                tool_name = item.name

                print()
                print(f"AI selected tool: {tool_name}")

                # ------------------------------------------------
                # READ TOOL ARGUMENTS
                # ------------------------------------------------

                try:
                    arguments = json.loads(item.arguments)

                except (json.JSONDecodeError, TypeError):
                    result = "The tool arguments could not be understood."

                else:

                    # ------------------------------------------------
                    # SECURITY CHECK
                    # ------------------------------------------------

                    if tool_name not in allowed_tool_names:
                        result = (
                            "This tool is not available to the selected "
                            "assistant."
                        )

                    # ------------------------------------------------
                    # RUN TOOL
                    # ------------------------------------------------

                    else:
                        result = run_tool(
                            tool_name,
                            arguments,
                        )

                print("Tool result:", result)

                # ------------------------------------------------
                # SEND TOOL RESULT BACK TO OPENAI
                # ------------------------------------------------

                tool_outputs.append(
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(result),
                    }
                )

            # ----------------------------------------------------
            # NO MORE TOOLS
            # ----------------------------------------------------

            if not tool_outputs:
                return response.output_text

            # ----------------------------------------------------
            # SECOND / FOLLOW-UP OPENAI REQUEST
            # ----------------------------------------------------

            response = client.responses.create(
                model="gpt-5.6",
                instructions=instructions,
                tools=assistant_tools,
                previous_response_id=response.id,
                input=tool_outputs,
            )

    # ------------------------------------------------------------
    # GENERAL ERROR HANDLING
    # ------------------------------------------------------------

    except Exception as error:

        return (
            "I'm sorry, I ran into a problem while "
            f"processing your request: {error}"
        )
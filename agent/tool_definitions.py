TOOLS = [
    # ============================================================
    # GENERAL TOOLS
    # ============================================================

    {
        "type": "function",
        "name": "calculator",
        "description": "Perform a mathematical calculation.",
        "parameters": {
            "type": "object",
            "properties": {
                "number1": {"type": "number"},
                "number2": {"type": "number"},
                "operation": {
                    "type": "string",
                    "enum": ["+", "-", "*", "/"],
                },
            },
            "required": ["number1", "number2", "operation"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "current_time",
        "description": "Get the current local time.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "weather",
        "description": "Get current weather information for Lagos.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
            },
            "required": ["city"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "web_search",
        "description": "Search the internet for current or recent information.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_results": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 5,
                },
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "save_note",
        "description": "Save information that the user specifically asks the AI to remember.",
        "parameters": {
            "type": "object",
            "properties": {
                "note": {"type": "string"},
            },
            "required": ["note"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "read_notes",
        "description": "Read information previously saved in the AI agent's notes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "delete_note",
        "description": "Delete a saved note when the user asks to forget or remove it.",
        "parameters": {
            "type": "object",
            "properties": {
                "note": {"type": "string"},
            },
            "required": ["note"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "list_tools",
        "description": "Tell the user what tools and capabilities the AI agent currently has.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },

    # ============================================================
    # VERIFIED AGENTS AND HOMES
    # COMPANY INFORMATION
    # ============================================================

    {
        "type": "function",
        "name": "get_company_information",
        "description": (
            "Provide general information about Verified Agents and Homes, "
            "including its name, tagline, description, purpose, and company information."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_company_services",
        "description": (
            "List the services provided by Verified Agents and Homes, "
            "including property verification, document search and verification, "
            "building approval verification, agent verification, and short-let verification."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_company_mission",
        "description": "Provide the mission of Verified Agents and Homes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_company_vision",
        "description": "Provide the vision of Verified Agents and Homes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_company_values",
        "description": "Provide the core values of Verified Agents and Homes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_company_story",
        "description": "Provide the story and background of Verified Agents and Homes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_company_commitment",
        "description": "Provide the commitment and customer-safety principles of Verified Agents and Homes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },

    # ============================================================
    # PROPERTY TOOLS
    # ============================================================

    {
        "type": "function",
        "name": "search_property",
        "description": (
            "Search for a property using its Property ID. "
            "Return basic property information such as location, property type, "
            "category, and overall property status. "
            "Do not use this when the user specifically asks for documents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "verify_property",
        "description": (
            "Verify a property using its Property ID. "
            "Use this when the user wants the overall verification status "
            "of a property or wants to know whether the property is verified."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "search_property_documents",
        "description": (
            "Search and list the individual document titles recorded for a property. "
            "Use this whenever the user asks to list, search, show, or see property documents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "verify_property_documents",
        "description": (
            "Verify the documents recorded for a property. "
            "Use this when the user specifically asks whether property documents are verified."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "search_land_documents",
        "description": (
            "Search and list land documents recorded for a property using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "verify_land_documents",
        "description": (
            "Verify land documents recorded for a property using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "search_house_documents",
        "description": (
            "Search and list house documents recorded for a property using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "verify_house_documents",
        "description": (
            "Verify house documents recorded for a property using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "search_location",
        "description": (
            "Search and recognize locations within Lagos State and return "
            "the relevant location information available in the Verified Agents and Homes data."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The Lagos State location, town, district, or LGA to search.",
                },
            },
            "required": ["location"],
            "additionalProperties": False,
        },
    },

    # ============================================================
    # SHORT-LET TOOLS
    # ============================================================

    {
        "type": "function",
        "name": "verify_shortlet_address",
        "description": (
            "Verify the address information recorded for a short-let property "
            "using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "verify_shortlet_owner",
        "description": (
            "Check the recorded verification information relating to the owner "
            "of a short-let property using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "verify_shortlet_manager",
        "description": (
            "Check the recorded verification information relating to the manager "
            "of a short-let property using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_shortlet_current_look",
        "description": (
            "Check the latest recorded current-look/update information for a short-let property. "
            "Use this when a customer wants to know whether the short-let's current condition "
            "or appearance has been recently updated."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_shortlet_reports",
        "description": (
            "Check reports or reported issues recorded against a short-let property."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"},
            },
            "required": ["property_id"],
            "additionalProperties": False,
        },
    },

    # ============================================================
    # VERIFIED AGENTS AND HOMES
    # AGENT TOOLS
    # ============================================================

    {
        "type": "function",
        "name": "search_agent",
        "description": (
            "Search for a Verified Agents and Homes real estate agent using the Agent ID. "
            "Return the agent's recorded basic information and verification information."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
            },
            "required": ["agent_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "search_agent_by_name",
        "description": (
            "Search for a Verified Agents and Homes real estate agent by the agent's "
            "name or agency name. Use this when the customer does not provide an Agent ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The agent's name or agency name.",
                },
            },
            "required": ["name"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "verify_agent",
        "description": (
            "Verify a real estate agent using the Agent ID. "
            "Return the recorded verification status, identity document status, "
            "and license status. Also remind the customer that the monthly "
            "VAH verification number must be checked before any transaction."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
            },
            "required": ["agent_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "search_agent_documents",
        "description": (
            "Search and list documents recorded for a real estate agent using the Agent ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
            },
            "required": ["agent_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "verify_agent_documents",
        "description": (
            "Verify documents recorded for a real estate agent using the Agent ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
            },
            "required": ["agent_id"],
            "additionalProperties": False,
        },
    },

    # ============================================================
    # MONTHLY AGENT UPDATE TOOLS
    # ============================================================

    {
        "type": "function",
        "name": "get_agent_monthly_update",
        "description": (
            "Check the latest monthly update recorded for a Verified Agents and Homes agent. "
            "Use this when the customer asks whether the agent's monthly verification information "
            "is current or wants the latest update."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
            },
            "required": ["agent_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_agent_reports",
        "description": (
            "Check reports recorded against a Verified Agents and Homes agent."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
            },
            "required": ["agent_id"],
            "additionalProperties": False,
        },
    },

    # ============================================================
    # MONTHLY VAH VERIFICATION NUMBER
    # ============================================================

    {
        "type": "function",
        "name": "get_vah_verification_number",
        "description": (
            "Retrieve the current VAH verification number recorded for a real estate agent. "
            "The VAH verification number is separate from the Agent ID and changes monthly. "
            "Use this when a customer asks for an agent's verification number, current verification "
            "number, monthly verification number, or wants to confirm that an agent's number is current. "
            "Always remind the customer to check the current Verified Agents and Homes database/platform "
            "immediately before transacting or paying an agent. Never tell the customer to rely on an old number."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
            },
            "required": ["agent_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_verification_statuses",
        "description": (
            "List the verification statuses used by Verified Agents and Homes "
            "and explain what they mean."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_payment_safety_guidance",
        "description": (
            "Provide safety guidance for customers before paying or transacting "
            "with a real estate agent, including checking the current VAH verification "
            "number and latest verification status."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },

    # ============================================================
    # DEWS AND AIRE NIG. LTD.
    # ============================================================

    {
        "type": "function",
        "name": "get_dews_aire_services",
        "description": (
            "List the services provided by Dews and Aire Nig. Ltd., including "
            "Architect / Interior Designer, Construction, Construction / Project Supervision, "
            "Property Management, and Short-let Booking."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_dews_aire_service",
        "description": (
            "Provide information about a specific service offered by Dews and Aire Nig. Ltd."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": "The Dews and Aire service the customer is asking about.",
                },
            },
            "required": ["service"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "recommend_dews_aire_service",
        "description": (
            "Identify which Dews and Aire Nig. Ltd. service best matches the customer's request."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "The customer's request or description of what they need.",
                },
            },
            "required": ["request"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "create_dews_aire_enquiry",
        "description": (
            "Prepare a Dews and Aire Nig. Ltd. customer enquiry for human follow-up."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "customer_request": {
                    "type": "string",
                    "description": "The customer's full request for follow-up.",
                },
            },
            "required": ["customer_request"],
            "additionalProperties": False,
        },
    },

    # ============================================================
    # JAHZ EMPIRE HOTEL & SUITES
    # ============================================================

    {
        "type": "function",
        "name": "get_jahz_hotel_services",
        "description": (
            "List the services and facilities available at JAHZ Empire Hotel & Suites, "
            "including hotel rooms and suites, events, bar and parties, swimming pool, "
            "swimming training, gym, gym instructors, hotel membership, Air Peace flight "
            "booking, and apartment or short-let accommodation."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_jahz_hotel_service",
        "description": (
            "Provide information about a specific service or facility offered by JAHZ Empire Hotel & Suites."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": "The JAHZ Empire Hotel & Suites service or facility.",
                },
            },
            "required": ["service"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "recommend_jahz_hotel_service",
        "description": (
            "Identify which JAHZ Empire Hotel & Suites service or facility best matches a customer's request."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "The customer's request or description of what they need.",
                },
            },
            "required": ["request"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "create_jahz_hotel_enquiry",
        "description": (
            "Prepare a JAHZ Empire Hotel & Suites customer enquiry for human follow-up."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "customer_request": {
                    "type": "string",
                    "description": "The customer's full request for hotel-team follow-up.",
                },
            },
            "required": ["customer_request"],
            "additionalProperties": False,
        },
    },

    # ============================================================
    # LAGOS MOVESMART
    # ============================================================

    {
        "type": "function",
        "name": "get_movesmart_categories",
        "description": (
            "List the categories of incidents and public problems that can be reported "
            "through Lagos MoveSmart."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_movesmart_category",
        "description": (
            "Provide information about a specific Lagos MoveSmart reporting category."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "The Lagos MoveSmart reporting category.",
                },
            },
            "required": ["category"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "recommend_movesmart_category",
        "description": (
            "Identify the most appropriate Lagos MoveSmart reporting category "
            "based on the user's description of a public problem or incident."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "report": {
                    "type": "string",
                    "description": "The user's description of the incident or public problem.",
                },
            },
            "required": ["report"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "create_movesmart_report",
        "description": (
            "Create a Lagos MoveSmart incident report from information supplied by the user."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "The incident category.",
                },
                "description": {
                    "type": "string",
                    "description": "A description of the incident.",
                },
                "location": {
                    "type": "string",
                    "description": "Where the incident occurred.",
                },
            },
            "required": ["category", "description", "location"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "get_movesmart_report_statuses",
        "description": (
            "List the statuses used to track Lagos MoveSmart reports."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "request_movesmart_evidence",
        "description": (
            "Request evidence or supporting information for a Lagos MoveSmart report."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "report_id": {
                    "type": "string",
                    "description": "The Lagos MoveSmart report ID.",
                },
                "evidence": {
                    "type": "string",
                    "description": "The evidence or supporting information.",
                },
            },
            "required": ["report_id", "evidence"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "create_movesmart_protected_information_request",
        "description": (
            "Create a protected-information request for a Lagos MoveSmart report "
            "when the user needs sensitive information handled through the appropriate process."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "report_id": {
                    "type": "string",
                    "description": "The Lagos MoveSmart report ID.",
                },
                "request": {
                    "type": "string",
                    "description": "The protected-information request.",
                },
            },
            "required": ["report_id", "request"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "create_movesmart_followup",
        "description": (
            "Create a follow-up request for an existing Lagos MoveSmart report."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "report_id": {
                    "type": "string",
                    "description": "The Lagos MoveSmart report ID.",
                },
                "message": {
                    "type": "string",
                    "description": "The follow-up message or request.",
                },
            },
            "required": ["report_id", "message"],
            "additionalProperties": False,
        },
    },
]
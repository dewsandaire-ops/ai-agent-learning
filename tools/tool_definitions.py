TOOLS = [
    # =========================
    # GENERAL TOOLS
    # =========================

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
                    "enum": ["+", "-", "*", "/"]
                }
            },
            "required": ["number1", "number2", "operation"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "current_time",
        "description": "Get the current local time.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "weather",
        "description": "Get current weather information for Lagos.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"],
            "additionalProperties": False
        }
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
                    "maximum": 5
                }
            },
            "required": ["query"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "save_note",
        "description": "Save information that the user specifically asks you to remember.",
        "parameters": {
            "type": "object",
            "properties": {
                "note": {"type": "string"}
            },
            "required": ["note"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "read_notes",
        "description": "Read information previously saved in the agent's notes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "delete_note",
        "description": "Delete a saved note when the user asks to forget or remove it.",
        "parameters": {
            "type": "object",
            "properties": {
                "note": {"type": "string"}
            },
            "required": ["note"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "list_tools",
        "description": "Tell the user what tools and capabilities the AI agent currently has.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    # =========================
    # VERIFIED AGENTS AND HOMES
    # COMPANY INFORMATION
    # =========================

    {
        "type": "function",
        "name": "get_company_information",
        "description": (
            "Provide general information about Verified Agents and Homes, "
            "including what the company does and its property, agent, "
            "and short-let verification services."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_company_services",
        "description": (
            "List the services provided by Verified Agents and Homes, "
            "including land and house document search and verification, "
            "property verification, building approval verification, "
            "real-estate agent verification, agent document verification, "
            "short-let address verification, short-let owner verification, "
            "short-let manager verification, monthly verification updates, "
            "and reporting of verification concerns."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_company_mission",
        "description": (
            "Provide the mission of Verified Agents and Homes."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_company_vision",
        "description": (
            "Provide the vision of Verified Agents and Homes."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_company_values",
        "description": (
            "Provide the core values of Verified Agents and Homes."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_company_story",
        "description": (
            "Provide the story and purpose behind Verified Agents and Homes."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_company_commitment",
        "description": (
            "Explain Verified Agents and Homes' commitment to verification, "
            "transparency, customer protection, and checking current "
            "information before transactions."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    # =========================
    # PROPERTY TOOLS
    # =========================

    {
        "type": "function",
        "name": "search_property",
        "description": (
            "Search for a property using its Property ID. "
            "Return only basic property information such as location, "
            "property type, category, and overall property status. "
            "Use this when the user asks about a property generally. "
            "Do NOT use this when the user specifically asks for document titles "
            "or property documents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "verify_property",
        "description": (
            "Verify a property using its Property ID. "
            "Return the property's overall status together with the recorded "
            "owner documents, land documents, house documents, and building approval. "
            "Use this when the user asks to verify the property as a whole."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "search_property_documents",
        "description": (
            "Search and list the individual document titles recorded for a property "
            "using its Property ID. Return the actual document names under Owner Documents, "
            "Land Documents, House Documents, and Building Approval. "
            "Use this whenever the user asks to list, search, show, or see "
            "the documents on record for a property."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "verify_property_documents",
        "description": (
            "Verify the individual documents recorded for a property using its Property ID. "
            "Use this when the user specifically asks whether the property's documents "
            "are verified, or asks for document verification."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "search_land_documents",
        "description": (
            "Search and list the individual land document titles recorded for a property "
            "using its Property ID. Use this when the user specifically asks for land documents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "verify_land_documents",
        "description": (
            "Verify the individual land documents recorded for a property using its Property ID. "
            "Use this when the user specifically asks to verify land documents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "search_house_documents",
        "description": (
            "Search and list the individual house document titles recorded for a property "
            "using its Property ID. Use this when the user specifically asks for house documents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "verify_house_documents",
        "description": (
            "Verify the individual house documents recorded for a property using its Property ID. "
            "Use this when the user specifically asks to verify house documents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "search_location",
        "description": (
            "Search and recognize locations within Lagos State. "
            "Use this when a user mentions a Lagos State location."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": (
                        "The Lagos State location, town, district, or LGA to search."
                    )
                }
            },
            "required": ["location"],
            "additionalProperties": False
        }
    },

    # =========================
    # SHORT-LET TOOLS
    # =========================

    {
        "type": "function",
        "name": "verify_shortlet_address",
        "description": (
            "Verify the address recorded for a short-let property using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "verify_shortlet_owner",
        "description": (
            "Verify the owner information recorded for a short-let property "
            "using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "verify_shortlet_manager",
        "description": (
            "Verify the manager information recorded for a short-let property "
            "using its Property ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_shortlet_current_look",
        "description": (
            "Return the latest recorded information about the current look or "
            "condition of a short-let property. Use this when a customer asks "
            "whether the current appearance or condition of a short-let has "
            "been recently updated."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_shortlet_reports",
        "description": (
            "Return reports or reported issues recorded against a short-let property. "
            "Use this when a customer asks whether there are reports, complaints, "
            "or issues associated with a short-let."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "property_id": {"type": "string"}
            },
            "required": ["property_id"],
            "additionalProperties": False
        }
    },

    # =========================
    # AGENT TOOLS
    # =========================

    {
        "type": "function",
        "name": "search_agent",
        "description": (
            "Search for a real estate agent using the Agent ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"}
            },
            "required": ["agent_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "search_agent_by_name",
        "description": (
            "Search for a real estate agent by the agent's name or agency name. "
            "Use this when the user provides an agent name or agency instead of an Agent ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The real estate agent's name or agency name."
                }
            },
            "required": ["name"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "verify_agent",
        "description": (
            "Verify a real estate agent and return the agent verification status, "
            "identity document status, license status, and current VAH Verification Number. "
            "The VAH Verification Number changes every month. "
            "Customers must check the latest database information before transacting."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"}
            },
            "required": ["agent_id"],
            "additionalProperties": False
        }
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
                "agent_id": {"type": "string"}
            },
            "required": ["agent_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "verify_agent_documents",
        "description": (
            "Verify the documents recorded for a real estate agent using the Agent ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"}
            },
            "required": ["agent_id"],
            "additionalProperties": False
        }
    },

    # =========================
    # MONTHLY AGENT UPDATE
    # =========================

    {
        "type": "function",
        "name": "get_agent_monthly_update",
        "description": (
            "Return the agent's monthly verification update information, "
            "including the update frequency, last update, next update, "
            "current address information, and address update status. "
            "Use this when a customer asks whether an agent's information "
            "has been recently updated."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"}
            },
            "required": ["agent_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_agent_reports",
        "description": (
            "Return reports recorded against a real estate agent. "
            "Use this when a customer asks whether an agent has reports, "
            "complaints, warnings, or concerns recorded against them."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"}
            },
            "required": ["agent_id"],
            "additionalProperties": False
        }
    },

    # =========================
    # VAH VERIFICATION NUMBER
    # =========================

    {
        "type": "function",
        "name": "get_vah_verification_number",
        "description": (
            "Return the current VAH Verification Number for a real estate agent. "
            "The VAH Verification Number is separate from the Agent ID and changes "
            "every month. Use this whenever a customer asks for an agent's "
            "verification number, current verification reference, or wants to "
            "confirm whether the number is current. Always remind the customer "
            "to check the latest Verified Agents and Homes database/platform "
            "immediately before making any transaction or payment. "
            "Never rely on an old month's verification number."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"}
            },
            "required": ["agent_id"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_verification_statuses",
        "description": (
            "List the verification statuses used by Verified Agents and Homes, "
            "including Submitted, Pending, Verified, Not Verified, Reported, "
            "Under Review, and Confirmed."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_payment_safety_guidance",
        "description": (
            "Provide payment and transaction safety guidance for customers "
            "dealing with real estate agents or properties. Emphasize that "
            "customers must confirm the current VAH Verification Number, "
            "latest verification status, monthly update, and any reports "
            "on the Verified Agents and Homes database/platform before "
            "making payment. Never treat an old verification number as current."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    # =========================
    # DEWS AND AIRE TOOLS
    # =========================

    {
        "type": "function",
        "name": "get_dews_aire_services",
        "description": (
            "List the services provided by Dews and Aire Nig. Ltd., "
            "including Architect / Interior Designer, Construction, "
            "Construction / Project Supervision, Property Management, "
            "and Short-let Booking."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_dews_aire_service",
        "description": (
            "Provide information about a specific service offered by "
            "Dews and Aire Nig. Ltd. Use this when a customer asks what "
            "a particular Dews and Aire service involves."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": "The Dews and Aire service the customer is asking about."
                }
            },
            "required": ["service"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "recommend_dews_aire_service",
        "description": (
            "Identify which Dews and Aire Nig. Ltd. service best matches "
            "a customer's request. Use this when the customer describes "
            "what they need without naming the service directly."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "The customer's request or description of what they need."
                }
            },
            "required": ["request"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_dews_aire_enquiry",
        "description": (
            "Prepare a Dews and Aire Nig. Ltd. customer enquiry for human "
            "follow-up. Use this when the customer has a request that "
            "requires a colleague to review or respond."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "customer_request": {
                    "type": "string",
                    "description": (
                        "The customer's full request that should be "
                        "forwarded for follow-up."
                    )
                }
            },
            "required": ["customer_request"],
            "additionalProperties": False
        }
    },

    # =========================
    # JAHZ EMPIRE HOTEL & SUITES
    # =========================

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
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_jahz_hotel_service",
        "description": (
            "Provide information about a specific service or facility offered by "
            "JAHZ Empire Hotel & Suites."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": (
                        "The JAHZ Empire Hotel & Suites service or facility "
                        "the customer is asking about."
                    )
                }
            },
            "required": ["service"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "recommend_jahz_hotel_service",
        "description": (
            "Identify which JAHZ Empire Hotel & Suites service or facility "
            "best matches a customer's request."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": (
                        "The customer's request or description of what "
                        "they need at JAHZ Empire Hotel & Suites."
                    )
                }
            },
            "required": ["request"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_jahz_hotel_enquiry",
        "description": (
            "Prepare a JAHZ Empire Hotel & Suites customer enquiry for human "
            "follow-up."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "customer_request": {
                    "type": "string",
                    "description": (
                        "The customer's full request that should be "
                        "prepared for hotel team follow-up."
                    )
                }
            },
            "required": ["customer_request"],
            "additionalProperties": False
        }
    },

    # =========================
    # LAGOS MOVESMART TOOLS
    # =========================

    {
        "type": "function",
        "name": "get_movesmart_categories",
        "description": (
            "List the types of public problems and incidents that can be "
            "reported through Lagos MoveSmart."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_movesmart_category",
        "description": (
            "Provide information about a specific Lagos MoveSmart report category."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": (
                        "The Lagos MoveSmart report category the user "
                        "is asking about."
                    )
                }
            },
            "required": ["category"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "recommend_movesmart_category",
        "description": (
            "Identify the most relevant Lagos MoveSmart report category "
            "or categories from a user's description of a public problem "
            "or incident."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "report_description": {
                    "type": "string",
                    "description": (
                        "The user's description of the problem or incident "
                        "they want to report."
                    )
                }
            },
            "required": ["report_description"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_movesmart_report",
        "description": (
            "Prepare a Lagos MoveSmart public report using the category, "
            "description, location, date and time, and available evidence."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "The category of the reported problem or incident."
                },
                "description": {
                    "type": "string",
                    "description": "A clear description of what happened or what was observed."
                },
                "location": {
                    "type": "string",
                    "description": "The location where the problem or incident occurred."
                },
                "date_time": {
                    "type": "string",
                    "description": "The date and time of the incident or observation."
                },
                "evidence": {
                    "type": "string",
                    "description": (
                        "Information about available photo or video evidence."
                    )
                }
            },
            "required": [
                "category",
                "description",
                "location",
                "date_time"
            ],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_movesmart_report_statuses",
        "description": (
            "Explain the stages of a Lagos MoveSmart report."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "request_movesmart_evidence",
        "description": (
            "Explain what evidence can support a Lagos MoveSmart report."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_movesmart_protected_information_request",
        "description": (
            "Prepare a request for protected information about another person. "
            "Do not disclose protected information merely because it was requested. "
            "Requests requiring authorization must remain pending authorized review."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "requested_information": {
                    "type": "string",
                    "description": (
                        "The information about another person that the requester "
                        "is asking for."
                    )
                },
                "reason": {
                    "type": "string",
                    "description": (
                        "The reason the requester says they need the information."
                    )
                },
                "authorization_documents": {
                    "type": "string",
                    "description": (
                        "Supporting authorization or document information."
                    )
                }
            },
            "required": [
                "requested_information",
                "reason"
            ],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_movesmart_followup",
        "description": (
            "Prepare a Lagos MoveSmart report or request for human review."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "report_or_request": {
                    "type": "string",
                    "description": (
                        "The full Lagos MoveSmart report or request "
                        "that requires human follow-up."
                    )
                }
            },
            "required": ["report_or_request"],
            "additionalProperties": False
        }
    },
]
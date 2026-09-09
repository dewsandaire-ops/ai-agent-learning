# ============================================================
# OPENAI TOOL DEFINITIONS
# ============================================================

TOOLS = [

    # ========================================================
    # VERIFIED AGENTS AND HOMES
    # ========================================================

    {
        "type": "function",
        "name": "get_shortlet_faq",
        "description": "Get frequently asked questions about short-let accommodation.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_car_hire_faq",
        "description": "Get frequently asked questions about car hire.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_verification_faq",
        "description": "Get frequently asked questions about verification.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_shortlet_house_rules",
        "description": "Get short-let house rules.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_combined_booking_faq",
        "description": "Get combined booking frequently asked questions.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_payment_safety_guidance",
        "description": "Get payment safety guidance from Verified Agents and Homes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_all_faqs",
        "description": "Get all available Verified Agents and Homes FAQs.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "search_faq",
        "description": "Search Verified Agents and Homes FAQs.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The customer's FAQ search question."
                },
                "section": {
                    "type": ["string", "null"],
                    "description": "Optional FAQ section."
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of results.",
                    "minimum": 1,
                    "maximum": 20
                }
            },
            "required": ["query"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_faq_answer",
        "description": "Get the best FAQ answer for a customer question.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "Customer question."
                },
                "section": {
                    "type": ["string", "null"],
                    "description": "Optional FAQ section."
                }
            },
            "required": ["question"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_faq_categories",
        "description": "Get available Verified Agents and Homes FAQ categories.",
        "parameters": {
            "type": "object",
            "properties": {
                "section": {
                    "type": ["string", "null"],
                    "description": "Optional FAQ section."
                }
            },
            "additionalProperties": False
        }
    },


    # ========================================================
    # DEWS AND AIRE
    # ========================================================

    {
        "type": "function",
        "name": "get_dews_aire_company_info",
        "description": "Get general company information about Dews and Aire Nig. Ltd.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_dews_aire_services",
        "description": "Get all Dews and Aire Nig. Ltd. services.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_dews_aire_service",
        "description": "Get information about a specific Dews and Aire service.",
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": "The Dews and Aire service to ask about."
                }
            },
            "required": ["service"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "recommend_dews_aire_service",
        "description": "Recommend an appropriate Dews and Aire service based on the customer's request.",
        "parameters": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "What the customer is requesting or needs help with."
                }
            },
            "required": ["request"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_dews_aire_faq_category",
        "description": "Get Dews and Aire FAQs for a specific category.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "FAQ category."
                }
            },
            "required": ["category"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_dews_aire_faqs",
        "description": "Get all Dews and Aire FAQs.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "search_dews_aire_faq",
        "description": "Search Dews and Aire FAQs using a customer's question.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_question": {
                    "type": "string",
                    "description": "The customer's question."
                }
            },
            "required": ["customer_question"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_dews_aire_enquiry",
        "description": "Create a Dews and Aire customer enquiry.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_request": {
                    "type": "string",
                    "description": "The customer's enquiry or request."
                }
            },
            "required": ["customer_request"],
            "additionalProperties": False
        }
    },


    # ========================================================
    # JAHZ EMPIRE HOTEL & SUITES
    # ========================================================

    {
        "type": "function",
        "name": "get_jahz_hotel_services",
        "description": "Get all JAHZ Empire Hotel and Suites services and facilities.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_jahz_hotel_service",
        "description": "Get information about a specific JAHZ hotel service or facility.",
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": "The hotel service or facility."
                }
            },
            "required": ["service"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_jahz_hotel_faq",
        "description": "Get frequently asked questions and answers about JAHZ Empire Hotel and Suites.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "search_jahz_hotel_faq",
        "description": "Search JAHZ hotel FAQs for the customer's question.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_question": {
                    "type": "string",
                    "description": "The customer's hotel question."
                }
            },
            "required": ["customer_question"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "recommend_jahz_hotel_service",
        "description": "Recommend an appropriate JAHZ hotel service or facility.",
        "parameters": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "What the customer needs or is requesting."
                }
            },
            "required": ["request"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_jahz_hotel_enquiry",
        "description": "Create a JAHZ Empire Hotel and Suites customer enquiry.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_request": {
                    "type": "string",
                    "description": "The customer's hotel enquiry or request."
                }
            },
            "required": ["customer_request"],
            "additionalProperties": False
        }
    },


    # ========================================================
    # LAGOS MOVESMART
    # ========================================================

    {
        "type": "function",
        "name": "get_movesmart_categories",
        "description": "Get all Lagos MoveSmart report categories.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_movesmart_category",
        "description": "Get information about a specific Lagos MoveSmart category.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "MoveSmart category."
                }
            },
            "required": ["category"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "recommend_movesmart_category",
        "description": "Recommend the most appropriate MoveSmart reporting category.",
        "parameters": {
            "type": "object",
            "properties": {
                "report_description": {
                    "type": "string",
                    "description": "Description of the problem the customer wants to report."
                }
            },
            "required": ["report_description"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_movesmart_faqs",
        "description": "Get all Lagos MoveSmart FAQs.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_movesmart_faq_section",
        "description": "Get Lagos MoveSmart FAQs for a specific section.",
        "parameters": {
            "type": "object",
            "properties": {
                "section": {
                    "type": "string",
                    "description": "MoveSmart FAQ section."
                }
            },
            "required": ["section"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_movesmart_faq",
        "description": "Get an answer to a Lagos MoveSmart FAQ question.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The customer's question."
                }
            },
            "required": ["question"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "answer_movesmart_question",
        "description": "Answer a Lagos MoveSmart question using available FAQ and reporting guidance.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The customer's question."
                }
            },
            "required": ["question"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_movesmart_report",
        "description": "Create a Lagos MoveSmart incident report.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Report category."
                },
                "description": {
                    "type": "string",
                    "description": "Description of the problem."
                },
                "location": {
                    "type": "string",
                    "description": "Location of the incident."
                },
                "date_time": {
                    "type": "string",
                    "description": "Date and time of the incident."
                },
                "evidence": {
                    "type": "string",
                    "description": "Evidence details, if available."
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
        "description": "Get available Lagos MoveSmart report statuses.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "request_movesmart_evidence",
        "description": "Request evidence for a Lagos MoveSmart report.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_movesmart_reward_information",
        "description": "Get information about Lagos MoveSmart reporting rewards.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "get_movesmart_emergency_guidance",
        "description": "Get Lagos MoveSmart emergency guidance.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "create_movesmart_protected_information_request",
        "description": "Create a Lagos MoveSmart request concerning protected information.",
        "parameters": {
            "type": "object",
            "properties": {
                "requested_information": {
                    "type": "string",
                    "description": "The protected information being requested."
                },
                "reason": {
                    "type": "string",
                    "description": "Reason for requesting the protected information."
                },
                "authorization_documents": {
                    "type": "string",
                    "description": "Authorization documents or details, if available."
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
        "description": "Create a follow-up concerning a Lagos MoveSmart report or request.",
        "parameters": {
            "type": "object",
            "properties": {
                "report_or_request": {
                    "type": "string",
                    "description": "The report or request that the customer wants to follow up on."
                }
            },
            "required": ["report_or_request"],
            "additionalProperties": False
        }
    },
]


# ============================================================
# ASSISTANT-SPECIFIC TOOL GROUPS
# ============================================================

TOOL_NAMES_BY_ASSISTANT = {

    # ========================================================
    # VENUS
    # ========================================================

    "venus": {
        "get_shortlet_faq",
        "get_car_hire_faq",
        "get_verification_faq",
        "get_shortlet_house_rules",
        "get_combined_booking_faq",
        "get_payment_safety_guidance",
        "get_all_faqs",
        "search_faq",
        "get_faq_answer",
        "get_faq_categories",
    },


    # ========================================================
    # DEWS
    # ========================================================

    "dews": {
        "get_dews_aire_company_info",
        "get_dews_aire_services",
        "get_dews_aire_service",
        "recommend_dews_aire_service",
        "get_dews_aire_faq_category",
        "get_dews_aire_faqs",
        "search_dews_aire_faq",
        "create_dews_aire_enquiry",
    },


    # ========================================================
    # JAHZ
    # ========================================================

    "jahz": {
        "get_jahz_hotel_services",
        "get_jahz_hotel_service",
        "get_jahz_hotel_faq",
        "search_jahz_hotel_faq",
        "recommend_jahz_hotel_service",
        "create_jahz_hotel_enquiry",
    },


    # ========================================================
    # LAGOS MOVESMART
    # ========================================================

    "movesmart": {
        "get_movesmart_categories",
        "get_movesmart_category",
        "recommend_movesmart_category",
        "get_movesmart_faqs",
        "get_movesmart_faq_section",
        "get_movesmart_faq",
        "answer_movesmart_question",
        "create_movesmart_report",
        "get_movesmart_report_statuses",
        "request_movesmart_evidence",
        "get_movesmart_reward_information",
        "get_movesmart_emergency_guidance",
        "create_movesmart_protected_information_request",
        "create_movesmart_followup",
    },
}


# ============================================================
# BUILD TOOL LISTS FOR EACH ASSISTANT
# ============================================================

TOOLS_BY_ASSISTANT = {}

for assistant_name, tool_names in TOOL_NAMES_BY_ASSISTANT.items():
    TOOLS_BY_ASSISTANT[assistant_name] = [
        tool
        for tool in TOOLS
        if tool.get("name") in tool_names
    ]
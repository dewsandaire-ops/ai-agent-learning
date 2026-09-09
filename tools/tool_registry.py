# ============================================================
# TOOL REGISTRY
# ============================================================
# This file connects the AI brain to the actual Python tools.
# Each assistant only receives access to its own business tools.
# ============================================================


from tools.dews_aire_tool import (
    create_dews_aire_enquiry,
    get_dews_aire_company_info,
    get_dews_aire_faq_category,
    get_dews_aire_faqs,
    get_dews_aire_service,
    get_dews_aire_services,
    recommend_dews_aire_service,
    search_dews_aire_faq,
)
from tools.jahz_hotel_tool import (
    create_jahz_hotel_enquiry,
    get_jahz_hotel_faq,
    get_jahz_hotel_service,
    get_jahz_hotel_services,
    recommend_jahz_hotel_service,
    search_jahz_hotel_faq,
)
from tools.movesmart_tool import (
    answer_movesmart_question,
    create_movesmart_followup,
    create_movesmart_protected_information_request,
    create_movesmart_report,
    get_movesmart_categories,
    get_movesmart_category,
    get_movesmart_emergency_guidance,
    get_movesmart_faq,
    get_movesmart_faq_section,
    get_movesmart_faqs,
    get_movesmart_report_statuses,
    get_movesmart_reward_information,
    recommend_movesmart_category,
    request_movesmart_evidence,
)
from tools.verified_agents_and_homes import (
    get_all_faqs,
    get_car_hire_faq,
    get_combined_booking_faq,
    get_faq_answer,
    get_faq_categories,
    get_payment_safety_guidance,
    get_shortlet_faq,
    get_shortlet_house_rules,
    get_verification_faq,
    search_faq,
)


# ============================================================
# ALL TOOLS
# ============================================================

TOOL_REGISTRY = {

    # --------------------------------------------------------
    # VERIFIED AGENTS AND HOMES
    # --------------------------------------------------------

    "get_all_faqs": get_all_faqs,
    "get_car_hire_faq": get_car_hire_faq,
    "get_combined_booking_faq": get_combined_booking_faq,
    "get_faq_answer": get_faq_answer,
    "get_faq_categories": get_faq_categories,
    "get_payment_safety_guidance": get_payment_safety_guidance,
    "get_shortlet_faq": get_shortlet_faq,
    "get_shortlet_house_rules": get_shortlet_house_rules,
    "get_verification_faq": get_verification_faq,
    "search_faq": search_faq,


    # --------------------------------------------------------
    # DEWS AND AIRE
    # --------------------------------------------------------

    "create_dews_aire_enquiry": create_dews_aire_enquiry,
    "get_dews_aire_company_info": get_dews_aire_company_info,
    "get_dews_aire_faq_category": get_dews_aire_faq_category,
    "get_dews_aire_faqs": get_dews_aire_faqs,
    "get_dews_aire_service": get_dews_aire_service,
    "get_dews_aire_services": get_dews_aire_services,
    "recommend_dews_aire_service": recommend_dews_aire_service,
    "search_dews_aire_faq": search_dews_aire_faq,


    # --------------------------------------------------------
    # JAHZ EMPIRE HOTEL & SUITES
    # --------------------------------------------------------

    "create_jahz_hotel_enquiry": create_jahz_hotel_enquiry,
    "get_jahz_hotel_faq": get_jahz_hotel_faq,
    "get_jahz_hotel_service": get_jahz_hotel_service,
    "get_jahz_hotel_services": get_jahz_hotel_services,
    "recommend_jahz_hotel_service": recommend_jahz_hotel_service,
    "search_jahz_hotel_faq": search_jahz_hotel_faq,


    # --------------------------------------------------------
    # LAGOS MOVESMART
    # --------------------------------------------------------

    "answer_movesmart_question": answer_movesmart_question,
    "create_movesmart_followup": create_movesmart_followup,
    "create_movesmart_protected_information_request": (
        create_movesmart_protected_information_request
    ),
    "create_movesmart_report": create_movesmart_report,
    "get_movesmart_categories": get_movesmart_categories,
    "get_movesmart_category": get_movesmart_category,
    "get_movesmart_emergency_guidance": get_movesmart_emergency_guidance,
    "get_movesmart_faq": get_movesmart_faq,
    "get_movesmart_faq_section": get_movesmart_faq_section,
    "get_movesmart_faqs": get_movesmart_faqs,
    "get_movesmart_report_statuses": get_movesmart_report_statuses,
    "get_movesmart_reward_information": get_movesmart_reward_information,
    "recommend_movesmart_category": recommend_movesmart_category,
    "request_movesmart_evidence": request_movesmart_evidence,
}


# ============================================================
# ASSISTANT-SPECIFIC TOOL NAMES
# ============================================================

VENUS_TOOLS = {
    "get_all_faqs",
    "get_car_hire_faq",
    "get_combined_booking_faq",
    "get_faq_answer",
    "get_faq_categories",
    "get_payment_safety_guidance",
    "get_shortlet_faq",
    "get_shortlet_house_rules",
    "get_verification_faq",
    "search_faq",
}


DEWS_TOOLS = {
    "create_dews_aire_enquiry",
    "get_dews_aire_company_info",
    "get_dews_aire_faq_category",
    "get_dews_aire_faqs",
    "get_dews_aire_service",
    "get_dews_aire_services",
    "recommend_dews_aire_service",
    "search_dews_aire_faq",
}


JAHZ_TOOLS = {
    "create_jahz_hotel_enquiry",
    "get_jahz_hotel_faq",
    "get_jahz_hotel_service",
    "get_jahz_hotel_services",
    "recommend_jahz_hotel_service",
    "search_jahz_hotel_faq",
}


MOVESMART_TOOLS = {
    "answer_movesmart_question",
    "create_movesmart_followup",
    "create_movesmart_protected_information_request",
    "create_movesmart_report",
    "get_movesmart_categories",
    "get_movesmart_category",
    "get_movesmart_emergency_guidance",
    "get_movesmart_faq",
    "get_movesmart_faq_section",
    "get_movesmart_faqs",
    "get_movesmart_report_statuses",
    "get_movesmart_reward_information",
    "recommend_movesmart_category",
    "request_movesmart_evidence",
}


# ============================================================
# TOOLS BY ASSISTANT
# ============================================================

TOOLS_BY_ASSISTANT_NAMES = {
    "venus": VENUS_TOOLS,
    "dews": DEWS_TOOLS,
    "jahz": JAHZ_TOOLS,
    "movesmart": MOVESMART_TOOLS,
}


# ============================================================
# GET TOOL
# ============================================================

def get_tool(tool_name):
    """Return a registered Python tool by name."""
    return TOOL_REGISTRY.get(tool_name)


# ============================================================
# GET TOOLS FOR ONE ASSISTANT
# ============================================================

def get_tools_for_assistant(assistant):
    """
    Return the Python tools belonging to one assistant.
    """

    assistant = str(assistant or "").strip().lower()

    tool_names = TOOLS_BY_ASSISTANT_NAMES.get(
        assistant,
        set()
    )

    return {
        name: TOOL_REGISTRY[name]
        for name in tool_names
        if name in TOOL_REGISTRY
    }
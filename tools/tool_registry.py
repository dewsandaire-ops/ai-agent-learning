from tools.dews_aire_tool import (
    create_dews_aire_enquiry,
    get_dews_aire_service,
    get_dews_aire_services,
    recommend_dews_aire_service,
)
from tools.jahz_hotel_tool import (
    create_jahz_hotel_enquiry,
    get_jahz_hotel_service,
    get_jahz_hotel_services,
    recommend_jahz_hotel_service,
)
from tools.movesmart_tool import (
    create_movesmart_followup,
    create_movesmart_protected_information_request,
    create_movesmart_report,
    get_movesmart_categories,
    get_movesmart_category,
    get_movesmart_report_statuses,
    recommend_movesmart_category,
    request_movesmart_evidence,
)
from tools.verified_agents_and_homes import (
    find_lagos_location,
    get_agent_monthly_update,
    get_agent_reports,
    get_company_commitment,
    get_company_information,
    get_company_mission,
    get_company_services,
    get_company_story,
    get_company_values,
    get_company_vision,
    get_payment_safety_guidance,
    get_shortlet_current_look,
    get_shortlet_reports,
    get_vah_verification_number,
    get_verification_statuses,
    search_agent,
    search_agent_by_name,
    search_agent_documents,
    search_house_documents,
    search_land_documents,
    search_location,
    search_property,
    search_property_documents,
    verify_agent,
    verify_agent_documents,
    verify_house_documents,
    verify_land_documents,
    verify_property,
    verify_property_documents,
    verify_shortlet_address,
    verify_shortlet_manager,
    verify_shortlet_owner,
)


TOOLS = {
    # Verified Agents and Homes
    "find_lagos_location": find_lagos_location,
    "search_location": search_location,
    "get_company_information": get_company_information,
    "get_company_services": get_company_services,
    "get_company_mission": get_company_mission,
    "get_company_vision": get_company_vision,
    "get_company_values": get_company_values,
    "get_company_story": get_company_story,
    "get_company_commitment": get_company_commitment,
    "search_property": search_property,
    "verify_property": verify_property,
    "search_property_documents": search_property_documents,
    "verify_property_documents": verify_property_documents,
    "search_land_documents": search_land_documents,
    "verify_land_documents": verify_land_documents,
    "search_house_documents": search_house_documents,
    "verify_house_documents": verify_house_documents,
    "search_agent": search_agent,
    "search_agent_by_name": search_agent_by_name,
    "verify_agent": verify_agent,
    "search_agent_documents": search_agent_documents,
    "verify_agent_documents": verify_agent_documents,
    "get_agent_monthly_update": get_agent_monthly_update,
    "get_agent_reports": get_agent_reports,
    "get_vah_verification_number": get_vah_verification_number,
    "verify_shortlet_address": verify_shortlet_address,
    "verify_shortlet_owner": verify_shortlet_owner,
    "verify_shortlet_manager": verify_shortlet_manager,
    "get_shortlet_current_look": get_shortlet_current_look,
    "get_shortlet_reports": get_shortlet_reports,
    "get_verification_statuses": get_verification_statuses,
    "get_payment_safety_guidance": get_payment_safety_guidance,

    # Dews and Aire Nig. Ltd.
    "get_dews_aire_services": get_dews_aire_services,
    "get_dews_aire_service": get_dews_aire_service,
    "recommend_dews_aire_service": recommend_dews_aire_service,
    "create_dews_aire_enquiry": create_dews_aire_enquiry,

    # Lagos MoveSmart
    "get_movesmart_categories": get_movesmart_categories,
    "get_movesmart_category": get_movesmart_category,
    "recommend_movesmart_category": recommend_movesmart_category,
    "create_movesmart_report": create_movesmart_report,
    "get_movesmart_report_statuses": get_movesmart_report_statuses,
    "request_movesmart_evidence": request_movesmart_evidence,
    "create_movesmart_protected_information_request": (
        create_movesmart_protected_information_request
    ),
    "create_movesmart_followup": create_movesmart_followup,

    # JAHZ Empire Hotel & Suites
    "get_jahz_hotel_services": get_jahz_hotel_services,
    "get_jahz_hotel_service": get_jahz_hotel_service,
    "recommend_jahz_hotel_service": recommend_jahz_hotel_service,
    "create_jahz_hotel_enquiry": create_jahz_hotel_enquiry,
}


def get_tool(tool_name):
    """Return a registered tool by name."""
    return TOOLS.get(tool_name)


def get_tools():
    """Return all registered tools."""
    return TOOLS
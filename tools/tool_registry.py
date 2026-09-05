from tools.calculator import calculator
from tools.time_tool import current_time
from tools.weather import weather
from tools.web_search import web_search
from tools.notes_tool import save_note, read_notes, delete_note
from tools.tools_info import list_tools

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

from tools.dews_aire_tool import (
    get_dews_aire_information,
    get_dews_aire_services,
)

from tools.movesmart_tool import (
    get_movesmart_information,
    get_movesmart_services,
)

from tools.jahz_hotel_tool import (
    get_jahz_information,
    get_jahz_services,
)


TOOLS = {
    # ---------------------------------------------------------------
    # EXISTING GENERAL TOOLS
    # ---------------------------------------------------------------
    "calculator": calculator,
    "current_time": current_time,
    "weather": weather,
    "web_search": web_search,
    "save_note": save_note,
    "read_notes": read_notes,
    "delete_note": delete_note,
    "list_tools": list_tools,

    # ---------------------------------------------------------------
    # VERIFIED AGENTS AND HOMES
    # ---------------------------------------------------------------
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

    # ---------------------------------------------------------------
    # DEWS AND AIRE NIG. LTD.
    # ---------------------------------------------------------------
    "get_dews_aire_information": get_dews_aire_information,
    "get_dews_aire_services": get_dews_aire_services,

    # ---------------------------------------------------------------
    # LAGOS MOVE SMART
    # ---------------------------------------------------------------
    "get_movesmart_information": get_movesmart_information,
    "get_movesmart_services": get_movesmart_services,

    # ---------------------------------------------------------------
    # JAHZ EMPIRE AND SUITES
    # ---------------------------------------------------------------
    "get_jahz_information": get_jahz_information,
    "get_jahz_services": get_jahz_services,
}
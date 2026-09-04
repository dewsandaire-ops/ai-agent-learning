AGENTS = {
    "AG-001": {
        "name": "John Adewale",
        "phone": "08012345678",
        "agency": "Adewale Properties",
        "picture": "Recorded",
        "verification_status": "Verified",

        "identity_document": "Government ID",
        "identity_document_status": "Verified",

        "license": "Real Estate License",
        "license_status": "Verified",

        "agency_registration": "Agency Registration",
        "agency_registration_status": "Verified",

        "documents": {
            "Government ID": "Verified",
            "Real Estate License": "Verified",
            "Agency Registration": "Verified",
        },
    },

    "AG-002": {
        "name": "Sarah Okafor",
        "phone": "08023456789",
        "agency": "Sarah Homes",
        "picture": "Recorded",
        "verification_status": "Verification Pending",

        "identity_document": "Government ID",
        "identity_document_status": "Submitted",

        "license": "Real Estate License",
        "license_status": "Pending",

        "agency_registration": "Agency Registration",
        "agency_registration_status": "Submitted",

        "documents": {
            "Government ID": "Submitted",
            "Real Estate License": "Pending",
            "Agency Registration": "Submitted",
        },
    },

    "AG-003": {
        "name": "David Williams",
        "phone": "08034567890",
        "agency": "Williams Realty",
        "picture": "Recorded",
        "verification_status": "Verified",

        "identity_document": "Government ID",
        "identity_document_status": "Verified",

        "license": "Real Estate License",
        "license_status": "Verified",

        "agency_registration": "Agency Registration",
        "agency_registration_status": "Verified",

        "documents": {
            "Government ID": "Verified",
            "Real Estate License": "Verified",
            "Agency Registration": "Verified",
        },
    },
}


def _get_agent(agent_id):
    """Return an agent record using the Agent ID."""

    return AGENTS.get(agent_id)


def _format_documents(documents):
    """Format agent documents for display."""

    if not documents:
        return "- No document recorded"

    return "\n".join(
        f"- {document}"
        for document in documents
    )


def _format_document_status(documents):
    """Format agent documents together with their status."""

    if not documents:
        return "- No document recorded"

    return "\n".join(
        f"- {document}: {status}"
        for document, status in documents.items()
    )


def search_agent(agent_id):
    """Search for basic agent information using Agent ID."""

    agent_data = _get_agent(agent_id)

    if agent_data is None:
        return f"No agent was found with ID '{agent_id}'."

    return (
        f"Agent ID: {agent_id}\n"
        f"Name: {agent_data['name']}\n"
        f"Phone: {agent_data['phone']}\n"
        f"Agency: {agent_data['agency']}\n"
        f"Picture: {agent_data['picture']}\n"
        f"Verification Status: "
        f"{agent_data['verification_status']}"
    )


def search_agent_by_name(name):
    """Search for an agent by name or agency name."""

    search_term = name.strip().lower()

    if not search_term:
        return "Please provide an agent name or agency name."

    matches = []

    for agent_id, agent_data in AGENTS.items():
        agent_name = agent_data["name"].lower()
        agency_name = agent_data["agency"].lower()

        if (
            search_term in agent_name
            or search_term in agency_name
        ):
            matches.append(
                f"Agent ID: {agent_id}\n"
                f"Name: {agent_data['name']}\n"
                f"Phone: {agent_data['phone']}\n"
                f"Agency: {agent_data['agency']}\n"
                f"Verification Status: "
                f"{agent_data['verification_status']}"
            )

    if not matches:
        return f"No agent was found matching '{name}'."

    return (
        "Matching Agents\n\n"
        + "\n\n".join(matches)
    )


def verify_agent(agent_id):
    """Return the complete verification information for an agent."""

    agent_data = _get_agent(agent_id)

    if agent_data is None:
        return f"No agent was found with ID '{agent_id}'."

    return (
        f"Agent Verification\n"
        f"Agent ID: {agent_id}\n"
        f"Name: {agent_data['name']}\n"
        f"Agency: {agent_data['agency']}\n"
        f"Verification Status: "
        f"{agent_data['verification_status']}\n"
        f"Government ID: "
        f"{agent_data['identity_document_status']}\n"
        f"Real Estate License: "
        f"{agent_data['license_status']}\n"
        f"Agency Registration: "
        f"{agent_data['agency_registration_status']}"
    )


def search_agent_documents(agent_id):
    """Search for documents recorded for an agent."""

    agent_data = _get_agent(agent_id)

    if agent_data is None:
        return f"No agent was found with ID '{agent_id}'."

    documents = agent_data["documents"]

    return (
        f"Agent Documents\n"
        f"Agent ID: {agent_id}\n"
        f"Name: {agent_data['name']}\n"
        f"Documents:\n"
        f"{_format_documents(documents.keys())}"
    )


def verify_agent_documents(agent_id):
    """Verify the status of all documents belonging to an agent."""

    agent_data = _get_agent(agent_id)

    if agent_data is None:
        return f"No agent was found with ID '{agent_id}'."

    documents = agent_data["documents"]

    return (
        f"Agent Document Verification\n"
        f"Agent ID: {agent_id}\n"
        f"Name: {agent_data['name']}\n"
        f"Document Status:\n"
        f"{_format_document_status(documents)}"
    )
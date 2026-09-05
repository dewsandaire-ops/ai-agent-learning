DEWS_AIRE_SERVICES = {
    "architect_interior_designer": {
        "name": "Architect / Interior Designer",
        "description": (
            "Professional architectural and interior design services for "
            "residential, commercial, luxury, and other spaces. Services can "
            "include space planning, design concepts, furniture and material "
            "selection, finishes, lighting, colour schemes, interior styling, "
            "and design coordination."
        ),
    },

    "construction": {
        "name": "Construction",
        "description": (
            "Construction services for building and development projects. "
            "Services may include construction coordination, building works, "
            "renovation, finishing, and other project requirements."
        ),
    },

    "project_supervision": {
        "name": "Construction / Project Supervision",
        "description": (
            "Construction and project supervision services to help monitor "
            "project progress, workmanship, materials, quality, timelines, "
            "and coordination of work on site."
        ),
    },

    "property_management": {
        "name": "Property Management",
        "description": (
            "Property management services for property owners who need "
            "assistance with managing, maintaining, monitoring, or overseeing "
            "their properties."
        ),
    },

    "shortlet_booking": {
        "name": "Book a Shortlet",
        "description": (
            "Short-let accommodation services that help customers find and "
            "book suitable short-let accommodation."
        ),
    },
}


def get_dews_aire_services():
    results = []

    for service in DEWS_AIRE_SERVICES.values():
        results.append(
            f"- {service['name']}: {service['description']}"
        )

    return (
        "Dews and Aire Nig. Ltd. Services\n\n"
        + "\n".join(results)
    )


def get_dews_aire_service(service):
    search_term = service.strip().lower()

    for service_data in DEWS_AIRE_SERVICES.values():
        name = service_data["name"].lower()

        if (
            search_term in name
            or search_term in service_data["description"].lower()
        ):
            return (
                f"Dews and Aire Service\n"
                f"Service: {service_data['name']}\n"
                f"Description: {service_data['description']}"
            )

    return (
        f"No Dews and Aire service was found matching '{service}'. "
        f"Please ask about one of the company's listed services."
    )


def recommend_dews_aire_service(request):
    request_lower = request.strip().lower()

    recommendations = []

    keywords = {
        "architect_interior_designer": [
            "architect",
            "architecture",
            "interior",
            "interior design",
            "decorate",
            "decoration",
            "design my house",
            "design my home",
            "furniture",
            "space planning",
            "luxury home",
        ],

        "construction": [
            "build",
            "building",
            "construction",
            "construct",
            "renovation",
            "renovate",
            "develop",
            "development",
        ],

        "project_supervision": [
            "supervision",
            "supervise",
            "project management",
            "monitor construction",
            "monitor building",
            "site supervision",
            "site inspection",
            "contractor",
        ],

        "property_management": [
            "manage my property",
            "property management",
            "manage property",
            "property manager",
            "maintain my property",
            "maintenance",
            "manage my house",
            "manage my apartment",
        ],

        "shortlet_booking": [
            "shortlet",
            "short-let",
            "short let",
            "book accommodation",
            "accommodation",
            "temporary accommodation",
            "holiday apartment",
            "book apartment",
        ],
    }

    for service_key, service_keywords in keywords.items():
        for keyword in service_keywords:
            if keyword in request_lower:
                recommendations.append(service_key)
                break

    if not recommendations:
        return (
            "I need a little more information to recommend the right "
            "Dews and Aire service. Please tell me what you need help with."
        )

    unique_recommendations = []

    for recommendation in recommendations:
        if recommendation not in unique_recommendations:
            unique_recommendations.append(recommendation)

    results = []

    for recommendation in unique_recommendations:
        service_data = DEWS_AIRE_SERVICES[recommendation]

        results.append(
            f"- {service_data['name']}: "
            f"{service_data['description']}"
        )

    return (
        "Recommended Dews and Aire Service(s)\n\n"
        + "\n".join(results)
    )


def create_dews_aire_enquiry(customer_request):
    request = customer_request.strip()

    if not request:
        return (
            "No customer request was provided. "
            "Please provide the customer's request."
        )

    return (
        "Dews and Aire Customer Enquiry\n"
        "Status: Ready for Human Follow-up\n\n"
        f"Customer Request:\n{request}\n\n"
        "A Dews and Aire team member should review this enquiry "
        "and contact the customer with the appropriate response."
    )

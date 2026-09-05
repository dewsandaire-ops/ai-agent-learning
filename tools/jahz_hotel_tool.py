JAHZ_HOTEL_SERVICES = {
    "rooms_and_suites": {
        "name": "Hotel Rooms & Suites",
        "description": (
            "Accommodation in hotel rooms and suites for guests."
        ),
    },

    "room_booking": {
        "name": "Room Booking",
        "description": (
            "Customers can make enquiries about booking rooms and suites "
            "at JAHZ Empire Hotel & Suites."
        ),
    },

    "events": {
        "name": "Events",
        "description": (
            "The hotel provides spaces and facilities for events, parties, "
            "training, meetings, celebrations, and other social or corporate "
            "gatherings."
        ),
    },

    "bar_and_parties": {
        "name": "Bar & Parties",
        "description": (
            "The hotel has a bar and provides a space where customers can "
            "organize parties and social gatherings."
        ),
    },

    "swimming_pool": {
        "name": "Swimming Pool",
        "description": (
            "The hotel has a swimming pool. Customers can make enquiries "
            "about pool access and swimming activities."
        ),
    },

    "swimming_training": {
        "name": "Swimming Training",
        "description": (
            "Customers can enquire about swimming training and learning "
            "to swim at the hotel."
        ),
    },

    "gym": {
        "name": "Gym",
        "description": (
            "The hotel has a gym where customers can exercise and make "
            "enquiries about gym facilities and training."
        ),
    },

    "gym_instructors": {
        "name": "Gym Instructors",
        "description": (
            "Gym instructors are available to assist customers with "
            "their fitness and training activities."
        ),
    },

    "membership": {
        "name": "Hotel Membership",
        "description": (
            "Customers can become members of the hotel and may receive "
            "membership benefits such as discounts and other privileges."
        ),
    },

    "air_peace_flights": {
        "name": "Air Peace Flight Booking",
        "description": (
            "JAHZ Empire Hotel & Suites is an affiliate of Air Peace. "
            "Customers can make enquiries about booking Air Peace flights "
            "through the hotel."
        ),
    },

    "apartment_shortlet": {
        "name": "Apartment / Short-let Accommodation",
        "description": (
            "Customers can make enquiries about apartment or short-let "
            "accommodation and booking."
        ),
    },
}


def get_jahz_hotel_services():
    """Return all services and facilities offered by JAHZ Empire Hotel & Suites."""

    services = []

    for service in JAHZ_HOTEL_SERVICES.values():
        services.append(
            f"- {service['name']}: {service['description']}"
        )

    return (
        "JAHZ Empire Hotel & Suites\n"
        "Services and Facilities\n\n"
        + "\n".join(services)
    )


def get_jahz_hotel_service(service):
    """Return information about a specific JAHZ hotel service."""

    search_term = service.strip().lower()

    if not search_term:
        return "Please provide the hotel service you want information about."

    for service_data in JAHZ_HOTEL_SERVICES.values():
        name = service_data["name"].lower()
        description = service_data["description"].lower()

        if (
            search_term in name
            or search_term in description
        ):
            return (
                f"JAHZ Empire Hotel & Suites\n"
                f"Service: {service_data['name']}\n"
                f"Description: {service_data['description']}"
            )

    return (
        f"No JAHZ Empire Hotel & Suites service was found matching "
        f"'{service}'."
    )


def recommend_jahz_hotel_service(request):
    """Identify the JAHZ hotel service that best matches a customer request."""

    request_lower = request.strip().lower()

    if not request_lower:
        return "Please describe what you need help with."

    keywords = {
        "rooms_and_suites": [
            "room",
            "rooms",
            "suite",
            "suites",
            "hotel room",
            "hotel rooms",
            "accommodation",
        ],

        "room_booking": [
            "book a room",
            "book room",
            "room booking",
            "reserve a room",
            "reservation",
            "hotel booking",
        ],

        "events": [
            "event",
            "events",
            "conference",
            "meeting",
            "training",
            "wedding",
            "celebration",
            "function",
        ],

        "bar_and_parties": [
            "bar",
            "party",
            "parties",
            "organize a party",
            "social gathering",
            "drinks",
        ],

        "swimming_pool": [
            "pool",
            "swimming pool",
            "swim",
            "pool access",
        ],

        "swimming_training": [
            "swimming lesson",
            "swimming lessons",
            "learn to swim",
            "swimming training",
            "swim training",
        ],

        "gym": [
            "gym",
            "fitness",
            "workout",
            "exercise",
        ],

        "gym_instructors": [
            "gym instructor",
            "fitness instructor",
            "personal trainer",
            "trainer",
        ],

        "membership": [
            "membership",
            "become a member",
            "hotel member",
            "member benefits",
            "membership discount",
            "member discount",
        ],

        "air_peace_flights": [
            "air peace",
            "flight",
            "flights",
            "book a flight",
            "flight booking",
            "air ticket",
            "plane ticket",
        ],

        "apartment_shortlet": [
            "apartment",
            "shortlet",
            "short-let",
            "short let",
            "shortlet booking",
            "book an apartment",
            "book a shortlet",
        ],
    }

    matches = []

    for service_key, service_keywords in keywords.items():
        for keyword in service_keywords:
            if keyword in request_lower:
                matches.append(service_key)
                break

    if not matches:
        return (
            "I can help with JAHZ Empire Hotel & Suites services and facilities. "
            "Please tell me what you need, such as a room booking, event, gym, "
            "swimming pool, membership, short-let accommodation, or Air Peace flight."
        )

    unique_matches = []

    for match in matches:
        if match not in unique_matches:
            unique_matches.append(match)

    results = []

    for match in unique_matches:
        service_data = JAHZ_HOTEL_SERVICES[match]

        results.append(
            f"- {service_data['name']}: "
            f"{service_data['description']}"
        )

    return (
        "Relevant JAHZ Empire Hotel & Suites Service(s)\n\n"
        + "\n".join(results)
    )


def create_jahz_hotel_enquiry(customer_request):
    """Prepare a JAHZ hotel customer enquiry for human follow-up."""

    request = customer_request.strip()

    if not request:
        return (
            "No customer request was provided. "
            "Please provide the customer's request."
        )

    return (
        "JAHZ Empire Hotel & Suites Customer Enquiry\n"
        "Status: Ready for Human Follow-up\n\n"
        f"Customer Request:\n{request}\n\n"
        "A JAHZ Empire Hotel & Suites team member should review "
        "the enquiry and contact the customer with the appropriate response."
    )

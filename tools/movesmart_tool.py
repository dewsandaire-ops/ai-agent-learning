MOVESMART_CATEGORIES = {
    "road_and_traffic": {
        "name": "Road & Traffic Problems",
        "description": (
            "Reports about bad roads, damaged roads, blocked roads, traffic "
            "problems, dangerous road conditions, missing road signs, and "
            "other road or traffic-related problems."
        ),
    },

    "unsafe_driving": {
        "name": "Unsafe or Reckless Driving",
        "description": (
            "Reports about reckless driving, dangerous driving, speeding, "
            "driving against traffic, driving while distracted, or other "
            "unsafe driving behaviour."
        ),
    },

    "unsafe_commercial_vehicles": {
        "name": "Unsafe Commercial Vehicles",
        "description": (
            "Reports about commercial vehicles operating in unsafe or poor "
            "conditions, including vehicles without seat belts, side mirrors, "
            "proper windows, fuel tanks, or other important safety features."
        ),
    },

    "illegal_pickup_and_dropoff": {
        "name": "Unauthorized Commercial Pickup / Drop-off",
        "description": (
            "Reports about commercial vehicles picking up or dropping off "
            "passengers at unauthorized, dangerous, or inappropriate locations."
        ),
    },

    "environment_and_waste": {
        "name": "Environment & Waste",
        "description": (
            "Reports about indiscriminate dumping of refuse, littering, "
            "blocked drainage caused by waste, environmental pollution, "
            "and other environmental problems."
        ),
    },

    "drainage_and_flooding": {
        "name": "Drainage & Flooding",
        "description": (
            "Reports about blocked or damaged drainage, flooding, stagnant "
            "water, poor drainage systems, and related problems."
        ),
    },

    "streetlights_and_traffic_signals": {
        "name": "Streetlights & Traffic Signals",
        "description": (
            "Reports about damaged or non-functioning streetlights, traffic "
            "lights, traffic signals, road signs, and related infrastructure."
        ),
    },

    "public_infrastructure": {
        "name": "Public Infrastructure",
        "description": (
            "Reports about damaged or poorly maintained public infrastructure "
            "and facilities that affect the community."
        ),
    },

    "illegal_or_unsafe_structures": {
        "name": "Illegal or Unsafe Structures",
        "description": (
            "Reports about structures that appear unauthorized, dangerous, "
            "unsafe, abandoned, or otherwise problematic."
        ),
    },

    "public_safety": {
        "name": "Public Safety",
        "description": (
            "Reports about situations that may threaten public safety, "
            "including suspicious or dangerous activities."
        ),
    },

    "crime_and_security": {
        "name": "Crime & Security Reports",
        "description": (
            "Reports concerning suspected criminal activity or security "
            "incidents. Serious emergencies should also be reported directly "
            "to the appropriate emergency or law-enforcement authority."
        ),
    },

    "other_public_problems": {
        "name": "Other Public Problems",
        "description": (
            "Other problems observed by members of the public that may affect "
            "the development, safety, cleanliness, or general wellbeing of Lagos."
        ),
    },
}


REPORT_STATUSES = [
    "Reported",
    "Evidence Submitted",
    "Under Review",
    "Verified / Confirmed",
    "Referred / Action Taken",
]


def get_movesmart_categories():
    """Return the categories of problems that can be reported through Lagos MoveSmart."""

    categories = []

    for category in MOVESMART_CATEGORIES.values():
        categories.append(
            f"- {category['name']}: {category['description']}"
        )

    return (
        "Lagos MoveSmart Report Categories\n\n"
        + "\n".join(categories)
    )


def get_movesmart_category(category):
    """Return information about a specific Lagos MoveSmart report category."""

    search_term = category.strip().lower()

    if not search_term:
        return "Please provide the Lagos MoveSmart category you want information about."

    for category_data in MOVESMART_CATEGORIES.values():
        name = category_data["name"].lower()
        description = category_data["description"].lower()

        if (
            search_term in name
            or search_term in description
        ):
            return (
                "Lagos MoveSmart Category\n"
                f"Category: {category_data['name']}\n"
                f"Description: {category_data['description']}"
            )

    return (
        f"No Lagos MoveSmart category was found matching '{category}'."
    )


def recommend_movesmart_category(report_description):
    """Identify the most relevant Lagos MoveSmart report categories."""

    report = report_description.strip().lower()

    if not report:
        return "Please describe the problem you want to report."

    keywords = {
        "road_and_traffic": [
            "bad road",
            "bad roads",
            "road problem",
            "road damage",
            "damaged road",
            "blocked road",
            "traffic problem",
            "road sign",
            "dangerous road",
            "pothole",
            "potholes",
        ],

        "unsafe_driving": [
            "reckless driving",
            "dangerous driving",
            "speeding",
            "driving dangerously",
            "driving against traffic",
            "one way",
            "drunk driving",
            "driver sleeping",
            "driver asleep",
        ],

        "unsafe_commercial_vehicles": [
            "commercial vehicle",
            "bus",
            "danfo",
            "no seat belt",
            "no seatbelt",
            "no side mirror",
            "no mirrors",
            "no fuel tank",
            "no window",
            "nylon window",
            "broken seat",
            "bad seat",
            "unsafe vehicle",
            "unroadworthy vehicle",
        ],

        "illegal_pickup_and_dropoff": [
            "illegal pickup",
            "illegal pick up",
            "illegal dropoff",
            "illegal drop off",
            "unauthorized pickup",
            "unauthorized pick up",
            "unauthorized dropoff",
            "unauthorized drop off",
            "bus stop",
            "picking passengers",
        ],

        "environment_and_waste": [
            "dumping",
            "dump refuse",
            "dumping refuse",
            "garbage",
            "litter",
            "littering",
            "waste",
            "refuse",
            "dirty environment",
            "pollution",
        ],

        "drainage_and_flooding": [
            "flood",
            "flooding",
            "flooded",
            "drainage",
            "blocked drainage",
            "dirty drainage",
            "stagnant water",
        ],

        "streetlights_and_traffic_signals": [
            "streetlight",
            "street lights",
            "street lamp",
            "traffic light",
            "traffic signal",
            "broken traffic light",
            "broken streetlight",
        ],

        "public_infrastructure": [
            "public infrastructure",
            "public facility",
            "damaged facility",
            "broken facility",
            "poor infrastructure",
            "public building",
        ],

        "illegal_or_unsafe_structures": [
            "illegal building",
            "illegal structure",
            "unsafe building",
            "unsafe structure",
            "abandoned building",
            "dangerous building",
            "building collapse",
        ],

        "public_safety": [
            "public safety",
            "dangerous situation",
            "safety problem",
            "threat to public",
            "suspicious activity",
        ],

        "crime_and_security": [
            "kidnap",
            "kidnapping",
            "robbery",
            "thief",
            "theft",
            "crime",
            "criminal",
            "armed robbery",
            "security incident",
        ],
    }

    matches = []

    for category_key, category_keywords in keywords.items():
        for keyword in category_keywords:
            if keyword in report:
                matches.append(category_key)
                break

    if not matches:
        return (
            "No specific Lagos MoveSmart category was identified. "
            "The report can still be submitted under Other Public Problems."
        )

    unique_matches = []

    for match in matches:
        if match not in unique_matches:
            unique_matches.append(match)

    results = []

    for match in unique_matches:
        category_data = MOVESMART_CATEGORIES[match]

        results.append(
            f"- {category_data['name']}: "
            f"{category_data['description']}"
        )

    return (
        "Relevant Lagos MoveSmart Report Category / Categories\n\n"
        + "\n".join(results)
    )


def create_movesmart_report(
    category,
    description,
    location,
    date_time,
    evidence="Not provided",
):
    """
    Prepare a Lagos MoveSmart public report.

    A report is not automatically considered verified.
    """

    category = category.strip()
    description = description.strip()
    location = location.strip()
    date_time = date_time.strip()
    evidence = evidence.strip()

    if not category:
        return "Please provide the report category."

    if not description:
        return "Please provide a description of the problem."

    if not location:
        return "Please provide the location of the incident or problem."

    if not date_time:
        return "Please provide the date and time of the incident or observation."

    return (
        "Lagos MoveSmart Report\n"
        "Status: Reported\n\n"
        f"Category: {category}\n"
        f"Description: {description}\n"
        f"Location: {location}\n"
        f"Date / Time: {date_time}\n"
        f"Evidence: {evidence}\n\n"
        "Important: This report has been recorded as a report only. "
        "It has not been independently verified. Evidence and details "
        "may be reviewed before any incident is classified as "
        "Verified / Confirmed or referred for action."
    )


def get_movesmart_report_statuses():
    """Return the possible stages of a Lagos MoveSmart report."""

    return (
        "Lagos MoveSmart Report Statuses\n\n"
        + "\n".join(
            f"{number}. {status}"
            for number, status in enumerate(REPORT_STATUSES, start=1)
        )
    )


def request_movesmart_evidence():
    """Explain the evidence that can support a Lagos MoveSmart report."""

    return (
        "Lagos MoveSmart Evidence Guidance\n\n"
        "A report may be supported with:\n"
        "- Photo evidence\n"
        "- Video evidence\n"
        "- The location of the incident or problem\n"
        "- The date and time\n"
        "- A clear description of what happened or what was observed\n\n"
        "Evidence helps reviewers understand and assess the report. "
        "Submitting a report does not by itself mean that the allegation "
        "has been verified."
    )


def create_movesmart_protected_information_request(
    requested_information,
    reason,
    authorization_documents="Not provided",
):
    """
    Prepare a request for protected information about another person.

    Protected information must not be released merely because someone asks
    for it. Supporting authorization or required documents must be reviewed.
    """

    requested_information = requested_information.strip()
    reason = reason.strip()
    authorization_documents = authorization_documents.strip()

    if not requested_information:
        return "Please state the information being requested."

    if not reason:
        return "Please state the reason for requesting the information."

    if authorization_documents == "Not provided":
        return (
            "Protected Information Request\n"
            "Status: Authorization Required\n\n"
            f"Requested Information: {requested_information}\n"
            f"Reason: {reason}\n\n"
            "Protected information about another person cannot be released "
            "merely because it has been requested. Appropriate supporting "
            "documentation or authorization, such as a police report or "
            "other required authorization, must be provided and reviewed "
            "before the request can proceed."
        )

    return (
        "Protected Information Request\n"
        "Status: Submitted for Authorization Review\n\n"
        f"Requested Information: {requested_information}\n"
        f"Reason: {reason}\n"
        f"Supporting Documents / Authorization: {authorization_documents}\n\n"
        "The supporting documentation must be reviewed by the appropriate "
        "authorized person or authority before protected information can "
        "be released. The AI must not disclose protected information "
        "without the required authorization."
    )


def create_movesmart_followup(report_or_request):
    """Prepare a Lagos MoveSmart matter for human follow-up."""

    request = report_or_request.strip()

    if not request:
        return (
            "No Lagos MoveSmart request was provided. "
            "Please provide the report or request."
        )

    return (
        "Lagos MoveSmart Human Follow-up\n"
        "Status: Ready for Human Review\n\n"
        f"Report / Request:\n{request}\n\n"
        "A responsible team member or appropriate authority should "
        "review the matter and determine the next action."
    )
```python
# ============================================================
# LAGOS MOVESMART
# REPORT CATEGORIES, FAQS, STATUS & REPORTING FUNCTIONS
# ============================================================


# ============================================================
# REPORT CATEGORIES
# ============================================================

MOVESMART_CATEGORIES = {

    "road_and_traffic": {
        "name": "Road & Traffic Problems",
        "description": (
            "Reports about bad roads, damaged roads, potholes, blocked roads, "
            "traffic problems, dangerous road conditions, missing road signs, "
            "and other road or traffic-related problems."
        ),
    },

    "unsafe_driving": {
        "name": "Unsafe or Reckless Driving",
        "description": (
            "Reports about reckless driving, dangerous driving, speeding, "
            "driving against traffic, distracted driving, running red lights, "
            "dangerous overtaking, or other unsafe driving behaviour."
        ),
    },

    "unsafe_commercial_vehicles": {
        "name": "Unsafe Commercial Vehicles",
        "description": (
            "Reports about commercial vehicles operating in unsafe or poor "
            "conditions, including overloading, missing seat belts, missing "
            "side mirrors, damaged seats, broken windows, unsafe vehicle "
            "conditions, or other missing or defective safety features."
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
            "including dangerous or suspicious activities."
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


# ============================================================
# REPORT STATUSES
# ============================================================

REPORT_STATUSES = [
    "Reported",
    "Evidence Submitted",
    "Under Review",
    "Verified / Confirmed",
    "Referred to Appropriate Authority",
    "Action Taken",
]


# ============================================================
# CATEGORY KEYWORDS
# ============================================================

MOVESMART_CATEGORY_KEYWORDS = {

    "road_and_traffic": [
        "bad road",
        "bad roads",
        "road problem",
        "road damage",
        "damaged road",
        "blocked road",
        "traffic problem",
        "traffic congestion",
        "road sign",
        "missing road sign",
        "dangerous road",
        "road condition",
        "pothole",
        "potholes",
        "road collapse",
        "collapsed road",
        "failed road",
        "bad highway",
    ],

    "unsafe_driving": [
        "reckless driving",
        "reckless driver",
        "dangerous driving",
        "dangerous driver",
        "unsafe driving",
        "speeding",
        "driving dangerously",
        "driving against traffic",
        "driving in the wrong direction",
        "wrong direction",
        "one way",
        "driving on one way",
        "drunk driving",
        "driver sleeping",
        "driver asleep",
        "distracted driving",
        "using phone while driving",
        "using a phone while driving",
        "texting while driving",
        "beating traffic light",
        "running red light",
        "jumping traffic light",
        "dangerous overtaking",
        "wrong overtaking",
        "illegal overtaking",
    ],

    "unsafe_commercial_vehicles": [
        "commercial vehicle",
        "commercial bus",
        "bus",
        "danfo",
        "minibus",
        "korope",
        "taxi",
        "tricycle",
        "keke",
        "motorcycle",
        "okada",

        "overloading",
        "overloaded",
        "overload",
        "too many passengers",
        "carrying too many passengers",
        "passengers beyond capacity",
        "excess passengers",

        "no seat belt",
        "no seatbelt",
        "missing seat belt",
        "missing seatbelt",
        "no side mirror",
        "no mirrors",
        "no mirror",
        "broken mirror",
        "broken side mirror",

        "no fuel tank",
        "no proper fuel tank",
        "unsafe fuel tank",

        "no window",
        "broken window",
        "nylon window",

        "broken seat",
        "bad seat",
        "damaged seat",

        "unsafe vehicle",
        "unsafe bus",
        "unroadworthy vehicle",
        "unroadworthy",
        "poorly maintained vehicle",
        "poorly maintained",
        "bad vehicle",
        "damaged vehicle",
        "unsafe commercial vehicle",
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
        "dangerous pickup",
        "dangerous pick up",
        "dangerous dropoff",
        "dangerous drop off",
        "bus stop",
        "picking passengers",
        "picking up passengers",
        "dropping passengers",
        "dropping off passengers",
        "loading passengers",
        "unloading passengers",
        "loading by the roadside",
        "dropping passengers on the road",
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
        "environmental pollution",
        "pollution",
        "illegal dumping",
        "waste dumping",
    ],

    "drainage_and_flooding": [
        "flood",
        "flooding",
        "flooded",
        "drainage",
        "blocked drainage",
        "dirty drainage",
        "damaged drainage",
        "open drainage",
        "stagnant water",
        "waterlogging",
        "water logged",
        "poor drainage",
    ],

    "streetlights_and_traffic_signals": [
        "streetlight",
        "street lights",
        "street lamp",
        "broken streetlight",
        "broken street light",
        "traffic light",
        "traffic signal",
        "broken traffic light",
        "non functioning traffic light",
        "traffic sign",
        "damaged traffic sign",
    ],

    "public_infrastructure": [
        "public infrastructure",
        "public facility",
        "damaged facility",
        "broken facility",
        "poor infrastructure",
        "public building",
        "damaged public building",
        "broken public facility",
        "public property",
    ],

    "illegal_or_unsafe_structures": [
        "illegal building",
        "illegal structure",
        "unsafe building",
        "unsafe structure",
        "abandoned building",
        "dangerous building",
        "building collapse",
        "collapsed building",
        "dangerous structure",
        "abandoned structure",
    ],

    "public_safety": [
        "public safety",
        "dangerous situation",
        "safety problem",
        "threat to public",
        "threat to public safety",
        "suspicious activity",
        "dangerous activity",
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
        "burglary",
        "assault",
        "violent attack",
    ],
}


# ============================================================
# FAQ DATABASE
# ============================================================

MOVESMART_FAQS = {

    "reporting": {
        "name": "Reporting",
        "faqs": [

            {
                "question": "What can I report to Lagos Move Smart?",
                "answer": (
                    "You can report transport safety concerns and other public "
                    "problems covered by Lagos Move Smart, including reckless "
                    "or dangerous driving, unsafe commercial vehicles, "
                    "unauthorized pickup or drop-off, bad roads, flooding, "
                    "drainage problems, environmental and waste issues, "
                    "damaged infrastructure, unsafe structures, public safety "
                    "concerns, crime and security incidents, and other public "
                    "problems."
                ),
            },

            {
                "question": "Who can report an incident?",
                "answer": (
                    "Any member of the public who observes a problem or "
                    "transport safety concern in Lagos can submit a report."
                ),
            },

            {
                "question": "Do I need to be a passenger to report a transport problem?",
                "answer": (
                    "No. You can report a problem you observe as a passenger, "
                    "pedestrian, driver, resident, or other road user."
                ),
            },

            {
                "question": "Can I report an incident that happened to someone else?",
                "answer": (
                    "Yes. You may report an incident you witnessed or have "
                    "reliable information about. Please provide accurate "
                    "information and clearly distinguish what you personally "
                    "observed from information received from someone else."
                ),
            },

            {
                "question": "Can I report more than one incident?",
                "answer": (
                    "Yes. Each separate incident should preferably be submitted "
                    "as a separate report so that each problem can be reviewed "
                    "and tracked properly."
                ),
            },
        ],
    },


    "how_to_report": {
        "name": "How to Submit a Report",
        "faqs": [

            {
                "question": "How do I report a transport safety problem?",
                "answer": (
                    "Click the REPORT button, complete the reporting form, "
                    "provide the available details, and submit your report."
                ),
            },

            {
                "question": "What information should I provide?",
                "answer": (
                    "Where possible, provide the location, date and time, "
                    "vehicle details, a clear description of what happened "
                    "or what you observed, and photo or other evidence if "
                    "safely available."
                ),
            },

            {
                "question": "Do I need to provide a photo or video?",
                "answer": (
                    "Not necessarily. You can submit a report without a photo "
                    "or video. However, useful evidence can help reviewers "
                    "understand and assess the report. Never put yourself "
                    "in danger to obtain evidence."
                ),
            },

            {
                "question": "Can I report a problem without knowing the vehicle's registration number?",
                "answer": (
                    "Yes. Provide as many identifying details as you can, "
                    "such as the vehicle type, colour, route, location, "
                    "operator information, or other useful details."
                ),
            },

            {
                "question": "Can I report an incident after it has already happened?",
                "answer": (
                    "Yes, provided you can provide useful and reasonably "
                    "accurate information about the incident or problem."
                ),
            },
        ],
    },


    "safety_and_privacy": {
        "name": "Safety & Privacy",
        "faqs": [

            {
                "question": "Do I have to put myself in danger to collect evidence?",
                "answer": (
                    "No. Your safety comes first. Never put yourself in danger "
                    "to take photographs, record videos, obtain information, "
                    "or collect evidence."
                ),
            },

            {
                "question": "Should I confront a driver about unsafe driving?",
                "answer": (
                    "No. Do not confront, threaten, or provoke anyone involved. "
                    "Move to a safe location and submit your report when it is "
                    "safe to do so."
                ),
            },

            {
                "question": "Is my information kept confidential?",
                "answer": (
                    "Information submitted through Lagos Move Smart should be "
                    "handled in accordance with the platform's privacy policy "
                    "and applicable requirements. Do not assume that every "
                    "report or piece of information is completely anonymous "
                    "unless Lagos Move Smart specifically provides that option."
                ),
            },

            {
                "question": "Can I submit a report anonymously?",
                "answer": (
                    "Anonymous reporting depends on the reporting options "
                    "provided by Lagos Move Smart. Please use the reporting "
                    "form to see what information is required before submitting "
                    "a report."
                ),
            },
        ],
    },


    "review_and_verification": {
        "name": "Review & Verification",
        "faqs": [

            {
                "question": "What happens after I submit a report?",
                "answer": (
                    "Your report is recorded as a reported incident and may "
                    "be reviewed. Where necessary, the information and evidence "
                    "provided may be checked or verified before the report is "
                    "classified as Verified / Confirmed or referred for action."
                ),
            },

            {
                "question": "Does every report result in immediate action?",
                "answer": (
                    "No. Reports may require review, verification, additional "
                    "information, or referral before appropriate action can "
                    "be taken."
                ),
            },

            {
                "question": "How do you verify a report?",
                "answer": (
                    "Reports may be assessed using the information and evidence "
                    "provided. Where appropriate, additional verification may "
                    "be carried out before a report is classified as "
                    "Verified / Confirmed."
                ),
            },

            {
                "question": "What happens if my report cannot be verified?",
                "answer": (
                    "A report that cannot be sufficiently verified may not "
                    "result in enforcement action. However, the information "
                    "may still help identify patterns or recurring problems."
                ),
            },

            {
                "question": "Can I provide additional information after submitting a report?",
                "answer": (
                    "If follow-up information is supported by the reporting "
                    "system, you may provide additional information relating "
                    "to your report. Do not submit duplicate reports unless "
                    "you have significant new information."
                ),
            },
        ],
    },


    "authorities_and_action": {
        "name": "Authorities & Action",
        "faqs": [

            {
                "question": "Which authorities receive reported incidents?",
                "answer": (
                    "Reports requiring official intervention may be referred "
                    "to the appropriate transport, government, emergency, "
                    "law-enforcement, or other relevant authority depending "
                    "on the nature of the report."
                ),
            },

            {
                "question": "Does Lagos Move Smart itself arrest or penalise drivers?",
                "answer": (
                    "Lagos Move Smart reporting does not replace the relevant "
                    "government enforcement or law-enforcement authorities. "
                    "Any enforcement action, penalty, arrest, or prosecution "
                    "is determined by the appropriate authorized authority."
                ),
            },

            {
                "question": "Can I track what happens to my report?",
                "answer": (
                    "Where report tracking is available, the report may move "
                    "through stages such as Reported, Evidence Submitted, "
                    "Under Review, Verified / Confirmed, Referred to Appropriate "
                    "Authority, and Action Taken."
                ),
            },

            {
                "question": "Will reporting an incident guarantee that the driver will be punished?",
                "answer": (
                    "No. A report provides information for review and possible "
                    "action. Any enforcement decision rests with the appropriate "
                    "authorized authority."
                ),
            },
        ],
    },


    "rewards": {
        "name": "Rewards",
        "faqs": [

            {
                "question": "Do I get paid for reporting a transport safety problem?",
                "answer": (
                    "Eligible and verified reports may qualify for a reward, "
                    "subject to the applicable Lagos Move Smart reward "
                    "criteria and terms."
                ),
            },

            {
                "question": "How do I claim my reward?",
                "answer": (
                    "If your report qualifies for a reward, follow the reward "
                    "claim instructions provided by Lagos Move Smart after "
                    "the report has completed the required verification process."
                ),
            },

            {
                "question": "How much is the reward?",
                "answer": (
                    "The reward amount is subject to the applicable Lagos "
                    "Move Smart reward terms and eligibility criteria."
                ),
            },

            {
                "question": "What makes a report eligible for a reward?",
                "answer": (
                    "Eligibility may depend on factors such as whether the "
                    "report is genuine, sufficiently detailed, verifiable, "
                    "original, and meets the applicable reward criteria."
                ),
            },

            {
                "question": "Will every report receive a reward?",
                "answer": (
                    "No. Only reports that meet the applicable eligibility "
                    "requirements and are sufficiently verified may qualify "
                    "for a reward."
                ),
            },

            {
                "question": "Can I submit false reports to receive a reward?",
                "answer": (
                    "No. Reports must be truthful and submitted in good faith. "
                    "False, misleading, malicious, deliberately fabricated, "
                    "or duplicate reports should not qualify for rewards."
                ),
            },
        ],
    },


    "locations_and_vehicles": {
        "name": "Locations & Vehicles",
        "faqs": [

            {
                "question": "Can I report incidents anywhere in Lagos?",
                "answer": (
                    "You can report problems within the areas covered by "
                    "Lagos Move Smart. Provide the most accurate location "
                    "possible so that the report can be properly assessed."
                ),
            },

            {
                "question": "What types of vehicles can I report?",
                "answer": (
                    "Depending on the reporting category, you may report "
                    "problems involving commercial vehicles, buses, taxis, "
                    "motorcycles, tricycles, trucks, private vehicles, and "
                    "other road users or vehicles covered by the platform."
                ),
            },

            {
                "question": "Can I report dangerous driving by a private vehicle?",
                "answer": (
                    "Yes. Dangerous or reckless driving can be reported "
                    "where it falls within the scope of Lagos Move Smart."
                ),
            },

            {
                "question": "Can I report overloading?",
                "answer": (
                    "Yes. Overloading is a transport safety concern and can "
                    "be reported with the relevant vehicle and location details."
                ),
            },

            {
                "question": "Can I report a vehicle that appears poorly maintained or unsafe?",
                "answer": (
                    "Yes. Describe the specific safety concern you observed, "
                    "such as missing safety equipment, damaged components, "
                    "or other conditions that appear to make the vehicle unsafe."
                ),
            },

            {
                "question": "Can I report dangerous transport activities at a bus stop or loading point?",
                "answer": (
                    "Yes. You can report unsafe or unauthorized pickup and "
                    "drop-off activities where they create a transport safety "
                    "concern."
                ),
            },
        ],
    },


    "emergencies": {
        "name": "Emergencies",
        "faqs": [

            {
                "question": "Can I use Lagos Move Smart to report an emergency?",
                "answer": (
                    "Lagos Move Smart reporting should not replace emergency "
                    "services. For an immediate emergency or situation requiring "
                    "urgent assistance, contact the appropriate emergency or "
                    "law-enforcement authority rather than waiting for a normal "
                    "report to be reviewed."
                ),
            },

            {
                "question": "What should I do if I witness an accident or immediate danger?",
                "answer": (
                    "Prioritize your own safety. If immediate assistance is "
                    "required, contact the appropriate emergency service or "
                    "authority. You may submit a Lagos Move Smart report when "
                    "it is safe to do so."
                ),
            },
        ],
    },


    "accuracy_and_trust": {
        "name": "Accuracy & Trust",
        "faqs": [

            {
                "question": "Can I report a driver or operator I don't like?",
                "answer": (
                    "Reports should be based on genuine, observable safety "
                    "concerns or other reportable problems. Do not use the "
                    "reporting system for personal disputes, harassment, "
                    "retaliation, or deliberately false allegations."
                ),
            },

            {
                "question": "What happens if someone submits a false report about me?",
                "answer": (
                    "Reports may be reviewed and assessed using the available "
                    "information and evidence. A report is not automatically "
                    "treated as a confirmed allegation simply because it was "
                    "submitted."
                ),
            },

            {
                "question": "Can I submit the same incident more than once?",
                "answer": (
                    "Avoid duplicate submissions unless you have significant "
                    "new information. Duplicate reports can make review and "
                    "tracking more difficult."
                ),
            },

            {
                "question": "How do I know that my report has been received?",
                "answer": (
                    "After submitting a report, use the confirmation or "
                    "reference information provided by the reporting system, "
                    "if available. The initial status of a successfully "
                    "submitted report is 'Reported'."
                ),
            },
        ],
    },
}


# ============================================================
# GET ALL CATEGORIES
# ============================================================

def get_movesmart_categories():
    """Return all Lagos MoveSmart report categories."""

    categories = []

    for category in MOVESMART_CATEGORIES.values():
        categories.append(
            f"- {category['name']}: {category['description']}"
        )

    return (
        "Lagos MoveSmart Report Categories\n\n"
        + "\n".join(categories)
    )


# ============================================================
# GET ONE CATEGORY
# ============================================================

def get_movesmart_category(category):
    """Return information about a specific Lagos MoveSmart category."""

    search_term = category.strip().lower()

    if not search_term:
        return (
            "Please provide the Lagos MoveSmart category "
            "you want information about."
        )

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


# ============================================================
# RECOMMEND REPORT CATEGORY
# ============================================================

def recommend_movesmart_category(report_description):
    """
    Identify the most relevant Lagos MoveSmart report categories.

    The function can return multiple categories when a report contains
    more than one type of problem.
    """

    report = report_description.strip().lower()

    if not report:
        return "Please describe the problem you want to report."

    matches = []

    for category_key, category_keywords in MOVESMART_CATEGORY_KEYWORDS.items():

        for keyword in category_keywords:

            if keyword in report:
                matches.append(category_key)
                break

    # Remove duplicates while preserving order.
    unique_matches = []

    for match in matches:
        if match not in unique_matches:
            unique_matches.append(match)

    if not unique_matches:
        return (
            "No specific Lagos MoveSmart category was identified.\n\n"
            "Suggested category: Other Public Problems\n\n"
            "You can still submit the report with a clear description "
            "of the problem."
        )

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


# ============================================================
# GET ALL FAQS
# ============================================================

def get_movesmart_faqs():
    """Return all Lagos MoveSmart frequently asked questions."""

    results = [
        "Lagos MoveSmart Frequently Asked Questions",
        ""
    ]

    for section in MOVESMART_FAQS.values():

        results.append(
            f"## {section['name']}"
        )

        for faq in section["faqs"]:

            results.append(
                f"\nQ: {faq['question']}"
            )

            results.append(
                f"A: {faq['answer']}"
            )

        results.append("")

    return "\n".join(results).strip()


# ============================================================
# GET FAQ SECTION
# ============================================================

def get_movesmart_faq_section(section):
    """Return FAQs belonging to a specific FAQ section."""

    search_term = section.strip().lower()

    if not search_term:
        return "Please provide the FAQ section you want."

    for section_key, section_data in MOVESMART_FAQS.items():

        if (
            search_term in section_key.lower()
            or search_term in section_data["name"].lower()
        ):

            results = [
                f"Lagos MoveSmart FAQ: {section_data['name']}",
                ""
            ]

            for faq in section_data["faqs"]:

                results.append(
                    f"Q: {faq['question']}"
                )

                results.append(
                    f"A: {faq['answer']}"
                )

                results.append("")

            return "\n".join(results).strip()

    return (
        f"No Lagos MoveSmart FAQ section was found "
        f"matching '{section}'."
    )


# ============================================================
# SEARCH FAQ
# ============================================================

def get_movesmart_faq(faq_question):
    """Find the most relevant Lagos MoveSmart FAQ."""

    search_term = faq_question.strip().lower()

    if not search_term:
        return (
            "Please provide the Lagos MoveSmart question "
            "you want answered."
        )

    # Exact / partial phrase match first.
    for section in MOVESMART_FAQS.values():

        for faq in section["faqs"]:

            question = faq["question"].lower()
            answer = faq["answer"].lower()

            if (
                search_term in question
                or search_term in answer
            ):
                return (
                    "Lagos MoveSmart FAQ\n\n"
                    f"Question: {faq['question']}\n"
                    f"Answer: {faq['answer']}"
                )

    # Word-based matching.
    search_words = [
        word.strip(".,?!'\"")
        for word in search_term.split()
        if len(word) >= 4
    ]

    best_match = None
    best_score = 0

    for section in MOVESMART_FAQS.values():

        for faq in section["faqs"]:

            question_words = set(
                faq["question"].lower().split()
            )

            score = 0

            for word in search_words:

                if word in question_words:
                    score += 1

            if score > best_score:

                best_score = score
                best_match = faq

    if best_match and best_score >= 2:

        return (
            "Lagos MoveSmart FAQ\n\n"
            f"Question: {best_match['question']}\n"
            f"Answer: {best_match['answer']}"
        )

    return (
        f"No Lagos MoveSmart FAQ was found matching "
        f"'{faq_question}'."
    )


# ============================================================
# NATURAL LANGUAGE FAQ + CATEGORY ASSISTANT
# ============================================================

def answer_movesmart_question(user_question):
    """
    Answer a public user's Lagos MoveSmart question.

    The function first checks for an FAQ match. If the question appears
    to describe a reportable incident instead, it recommends a category.
    """

    question = user_question.strip()

    if not question:
        return (
            "Please ask a Lagos MoveSmart question or describe "
            "the problem you want to report."
        )

    faq_result = get_movesmart_faq(question)

    if not faq_result.startswith(
        "No Lagos MoveSmart FAQ was found"
    ):
        return faq_result

    category_result = recommend_movesmart_category(question)

    if not category_result.startswith(
        "No specific Lagos MoveSmart category was identified"
    ):
        return (
            "Your message appears to describe a reportable problem.\n\n"
            + category_result
            + "\n\n"
            "You can submit the incident through the Lagos MoveSmart "
            "REPORT option."
        )

    return (
        "I could not find a specific Lagos MoveSmart FAQ matching "
        "your question.\n\n"
        "You can ask about:\n"
        "- What you can report\n"
        "- How to submit a report\n"
        "- Evidence requirements\n"
        "- Report verification\n"
        "- Report status\n"
        "- Authorities and action\n"
        "- Rewards\n"
        "- Safety and privacy\n"
        "- Emergency situations\n\n"
        "You can also describe the problem you observed and I can "
        "help identify the most relevant report category."
    )


# ============================================================
# REPORT CREATION
# ============================================================

def create_movesmart_report(
    category,
    description,
    location,
    date_time,
    evidence="Not provided",
):
    """
    Prepare a Lagos MoveSmart public report.

    A newly submitted report is always recorded as 'Reported'.
    It is NOT automatically considered verified.
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
        return (
            "Please provide the date and time of the incident "
            "or observation."
        )

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
        "may be reviewed before the incident is classified as "
        "Verified / Confirmed or referred to an appropriate authority."
    )


# ============================================================
# REPORT STATUS INFORMATION
# ============================================================

def get_movesmart_report_statuses():
    """Return the possible stages of a Lagos MoveSmart report."""

    descriptions = {
        "Reported": (
            "The report has been submitted and recorded."
        ),

        "Evidence Submitted": (
            "Supporting evidence has been provided with the report."
        ),

        "Under Review": (
            "The report and available information are being reviewed."
        ),

        "Verified / Confirmed": (
            "The available information has been sufficiently verified "
            "or confirmed for the applicable reporting process."
        ),

        "Referred to Appropriate Authority": (
            "The matter has been referred to the relevant authority "
            "or responsible organization for appropriate consideration."
        ),

        "Action Taken": (
            "The system has received or recorded information indicating "
            "that action has been taken. This status does not by itself "
            "describe the specific enforcement outcome."
        ),
    }

    results = [
        "Lagos MoveSmart Report Statuses",
        ""
    ]

    for number, status in enumerate(
        REPORT_STATUSES,
        start=1
    ):

        results.append(
            f"{number}. {status}"
        )

        results.append(
            f"   {descriptions[status]}"
        )

    return "\n".join(results)


# ============================================================
# EVIDENCE GUIDANCE
# ============================================================

def request_movesmart_evidence():
    """Explain evidence that can support a Lagos MoveSmart report."""

    return (
        "Lagos MoveSmart Evidence Guidance\n\n"

        "A report may be supported with:\n"

        "- Photo evidence\n"
        "- Video evidence\n"
        "- The location of the incident or problem\n"
        "- The date and time\n"
        "- Vehicle registration or identifying details, where available\n"
        "- A clear description of what happened or what was observed\n\n"

        "Evidence can help reviewers understand and assess the report. "
        "Submitting a report does not by itself mean that the allegation "
        "has been verified.\n\n"

        "SAFETY FIRST:\n"
        "Never put yourself or another person in danger to obtain "
        "photographs, videos, or other evidence."
    )


# ============================================================
# REWARD INFORMATION
# ============================================================

def get_movesmart_reward_information():
    """Return the general Lagos MoveSmart reward policy."""

    return (
        "Lagos MoveSmart Reward Information\n\n"

        "Eligible and verified reports may qualify for a reward, "
        "subject to the applicable Lagos MoveSmart reward criteria "
        "and terms.\n\n"

        "Important:\n"
        "- Not every report qualifies for a reward.\n"
        "- A report must meet the applicable eligibility requirements.\n"
        "- Reports may need to be verified before reward eligibility "
        "is determined.\n"
        "- False, misleading, malicious, deliberately fabricated, "
        "or duplicate reports should not qualify.\n"
        "- The reward amount and claim procedure are subject to the "
        "applicable Lagos MoveSmart reward terms."
    )


# ============================================================
# EMERGENCY GUIDANCE
# ============================================================

def get_movesmart_emergency_guidance():
    """Return emergency reporting guidance."""

    return (
        "Lagos MoveSmart Emergency Guidance\n\n"

        "Lagos MoveSmart reporting should not replace emergency services.\n\n"

        "If you witness an immediate emergency, serious accident, "
        "violent incident, or situation requiring urgent assistance, "
        "prioritize your safety and contact the appropriate emergency "
        "or law-enforcement authority.\n\n"

        "You may submit a Lagos MoveSmart report when it is safe to do so.\n\n"

        "Never confront, chase, threaten, or attempt to physically stop "
        "a person involved in a dangerous situation."
    )


# ============================================================
# PROTECTED INFORMATION REQUEST
# ============================================================

def create_movesmart_protected_information_request(
    requested_information,
    reason,
    authorization_documents="Not provided",
):
    """
    Prepare a request for protected information about another person.

    Protected information must not be released merely because someone asks.
    Appropriate authorization or required documentation must be reviewed.
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
            "documentation or authorization must be provided and reviewed "
            "before the request can proceed."
        )

    return (
        "Protected Information Request\n"
        "Status: Submitted for Authorization Review\n\n"
        f"Requested Information: {requested_information}\n"
        f"Reason: {reason}\n"
        f"Supporting Documents / Authorization: "
        f"{authorization_documents}\n\n"
        "The supporting documentation must be reviewed by the appropriate "
        "authorized person or authority before protected information can "
        "be released. The AI must not disclose protected information "
        "without the required authorization."
    )


# ============================================================
# HUMAN FOLLOW-UP
# ============================================================

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
```

# ============================================================
# VERIFIED AGENTS AND HOMES
# FAQ DATABASE
# ============================================================

PAYMENT_SAFETY_NOTICE = """
Before making payment, guests, tenants, buyers, investors, and customers
are encouraged to confirm the property or short-let address, booking details,
applicable house rules, identification requirements, caution/security fee,
cancellation terms, and the identity and authorization of the person
receiving payment.

Verification by Verified Agents and Homes is intended to support due
diligence and informed decision-making. Verification does not constitute
an absolute guarantee against fraud, loss, ownership disputes, property
defects, service failures, or future changes.
"""


# ============================================================
# SHORT-LET HOUSE RULES
# ============================================================

SHORTLET_HOUSE_RULES = {
    "identification": (
        "A valid means of identification is required for guests. Accepted "
        "identification may include a NIN-related valid ID, international "
        "passport, driver's licence, or another valid government-issued ID, "
        "subject to the property's requirements."
    ),

    "check_in": (
        "Standard check-in is from 2:00 p.m. Early check-in may be available "
        "upon request and may attract an additional fee."
    ),

    "check_out": (
        "Check-out is from 11:00 a.m. and no later than 12:00 noon, unless "
        "otherwise stated by the property."
    ),

    "late_checkout": (
        "Late check-out may be available subject to availability and may "
        "attract a fee calculated according to the applicable property terms."
    ),

    "smoking": (
        "Indoor smoking is not permitted. A violation may result in "
        "forfeiture of the caution/security deposit and additional charges "
        "where applicable."
    ),

    "noise": (
        "Loud music, excessive noise, and activities that disturb neighbours "
        "or other residents are not permitted."
    ),

    "parties": (
        "Parties and gatherings are strictly prohibited in apartments unless "
        "the property has specifically been designated and approved for such "
        "events. Guests requiring an event or get-together space should ask "
        "for a suitable property."
    ),

    "occupancy": {
        "studio": 2,
        "1_bedroom": 2,
        "2_bedroom": 4,
        "3_bedroom": 6,
        "4_bedroom": 8,
    },

    "visitors": (
        "Additional guests or visitors must comply with the property's "
        "occupancy, security, identification, and estate rules. Guests should "
        "obtain approval before bringing additional people into the property."
    ),

    "children": (
        "Children may be permitted depending on the property. Parents or "
        "guardians remain responsible for children's safety and children "
        "must not be left unsupervised."
    ),

    "pets": (
        "Pets are not permitted unless a property specifically states "
        "otherwise."
    ),

    "furniture": (
        "Guests should not move furniture or remove property items from their "
        "designated locations without permission."
    ),

    "property_items": (
        "Items belonging to the apartment, estate, or property must not be "
        "taken outside the premises."
    ),

    "damage": (
        "Guests should report damage as soon as it is noticed. Damage caused "
        "by negligence or misuse may be deducted from the caution/security "
        "deposit. Where the cost exceeds the deposit, the guest may be "
        "required to pay the outstanding amount before checkout."
    ),

    "smart_card": (
        "Loss of an estate or apartment smart card may attract a replacement "
        "or administrative charge."
    ),

    "photoshoots": (
        "Photoshoots, video shoots, content production, and other commercial "
        "or professional productions may attract additional charges and "
        "require prior approval."
    ),

    "lights_and_ac": (
        "Guests should switch off lights, air conditioners, and electrical "
        "equipment when leaving the apartment."
    ),

    "doors_and_windows": (
        "Guests should close windows and securely lock the apartment door "
        "when leaving the property."
    ),

    "parking": (
        "Guests must comply with the parking rules and instructions of the "
        "property or estate."
    ),

    "vehicle_horns": (
        "Vehicle horns should not be used unnecessarily within the estate."
    ),

    "antisocial_behaviour": (
        "Antisocial behaviour includes conduct that threatens, harasses, "
        "disturbs, intimidates, damages property, or unreasonably interferes "
        "with other residents or guests."
    ),

    "security": (
        "Where provided by the property or estate, security may include "
        "24-hour security personnel and CCTV surveillance."
    ),

    "pool": (
        "Where a swimming pool is available, the usual operating period is "
        "10:00 a.m. to 6:00 p.m., subject to the property's rules and "
        "operating arrangements."
    ),

    "pool_safety": (
        "Guests must follow all swimming-pool safety instructions and "
        "children must be supervised by their parents or guardians."
    ),

    "housekeeping": (
        "Housekeeping is generally provided every two days, usually between "
        "9:00 a.m. and 2:00 p.m., or as otherwise required by the property."
    ),

    "daily_housekeeping": (
        "Daily housekeeping may be available at an additional charge."
    ),

    "extension": (
        "Guests who wish to extend their stay should provide at least "
        "24 hours' notice. Extensions are subject to availability."
    ),

    "inventory": (
        "A staff member or housekeeper may be present during check-in and "
        "check-out to conduct a basic inventory and inspect the apartment."
    ),

    "deposit_refund": (
        "The caution/security deposit is generally refunded after the "
        "apartment has been cleaned and inspected, provided there are no "
        "outstanding charges, damages, missing items, or applicable penalties."
    ),

    "rule_violations": (
        "Violation of house or estate rules may result in forfeiture of the "
        "caution/security deposit, additional charges, termination of the "
        "stay, or other applicable estate penalties."
    ),

    "estate_fine": (
        "Where applicable, an estate may impose a fine of up to ₦250,000 or "
        "another estate-imposed penalty for serious rule violations. The "
        "actual penalty depends on the applicable estate/property rules."
    ),
}


# ============================================================
# SHORT-LET FAQ
# ============================================================

SHORTLET_FAQ = [

    {
        "id": 1,
        "category": "Short-let Booking",
        "question": "How can I book a short-let apartment?",
        "answer": (
            "You can request a short-let by providing your preferred "
            "location, dates, number of guests, apartment type, and other "
            "requirements. Availability and booking terms depend on the "
            "property or provider."
        ),
    },
    {
        "id": 2,
        "category": "Short-let Booking",
        "question": "How do I know if a short-let apartment is available?",
        "answer": (
            "Availability must be confirmed with the property or authorized "
            "booking provider for your requested dates before payment."
        ),
    },
    {
        "id": 3,
        "category": "Short-let Booking",
        "question": "Can I book an apartment for one night?",
        "answer": (
            "Some apartments accept one-night bookings, while others have "
            "minimum-stay requirements. Availability and minimum stay depend "
            "on the property."
        ),
    },
    {
        "id": 4,
        "category": "Short-let Booking",
        "question": "What is the minimum stay required?",
        "answer": (
            "Minimum-stay requirements vary by apartment, provider, season, "
            "and booking period. Confirm the applicable requirement before "
            "payment."
        ),
    },
    {
        "id": 5,
        "category": "Short-let Booking",
        "question": "Can I extend my stay after checking in?",
        "answer": SHORTLET_HOUSE_RULES["extension"],
    },
    {
        "id": 6,
        "category": "Short-let Booking",
        "question": "How much notice is required to extend my stay?",
        "answer": (
            "At least 24 hours' notice is recommended and may be required. "
            "Extensions remain subject to availability."
        ),
    },
    {
        "id": 7,
        "category": "Check-in & Check-out",
        "question": "Can I request an early check-in?",
        "answer": (
            "Yes. Early check-in may be requested, but it is subject to "
            "availability and property approval."
        ),
    },
    {
        "id": 8,
        "category": "Check-in & Check-out",
        "question": "Is there a fee for early check-in?",
        "answer": (
            "An early check-in fee may apply depending on the property and "
            "how early you wish to check in."
        ),
    },
    {
        "id": 9,
        "category": "Check-in & Check-out",
        "question": "What time is check-in?",
        "answer": SHORTLET_HOUSE_RULES["check_in"],
    },
    {
        "id": 10,
        "category": "Check-in & Check-out",
        "question": "What time is check-out?",
        "answer": SHORTLET_HOUSE_RULES["check_out"],
    },
    {
        "id": 11,
        "category": "Check-in & Check-out",
        "question": "Is late check-out allowed?",
        "answer": SHORTLET_HOUSE_RULES["late_checkout"],
    },
    {
        "id": 12,
        "category": "Check-in & Check-out",
        "question": "Is there a fee for late check-out?",
        "answer": (
            "Yes, a late check-out fee may apply, usually according to the "
            "property's applicable hourly or fixed late-checkout charge."
        ),
    },
    {
        "id": 13,
        "category": "Cancellation",
        "question": "Can I cancel or change my booking?",
        "answer": (
            "Cancellation and modification terms vary by property and "
            "provider. Always confirm the applicable cancellation policy "
            "before making payment."
        ),
    },
    {
        "id": 14,
        "category": "Cancellation",
        "question": "What happens if I need to leave earlier than planned?",
        "answer": (
            "Early departure does not automatically entitle a guest to a "
            "refund. Any refund depends on the property's cancellation and "
            "early-departure policy."
        ),
    },

    # --------------------------------------------------------
    # GUEST REQUIREMENTS
    # --------------------------------------------------------

    {
        "id": 15,
        "category": "Guest Requirements",
        "question": "What identification is required when booking or checking in?",
        "answer": SHORTLET_HOUSE_RULES["identification"],
    },
    {
        "id": 16,
        "category": "Guest Requirements",
        "question": "What forms of identification are accepted?",
        "answer": (
            "Accepted identification may include a NIN-related valid ID, "
            "international passport, driver's licence, or another valid "
            "government-issued identification, subject to property rules."
        ),
    },
    {
        "id": 17,
        "category": "Guest Requirements",
        "question": "Do all guests need to provide identification?",
        "answer": (
            "The property or estate may require identification from all "
            "guests or occupants. Confirm the specific requirement before "
            "check-in."
        ),
    },
    {
        "id": 18,
        "category": "Guest Requirements",
        "question": "How many people can stay in the apartment?",
        "answer": (
            "The standard maximum occupancy is 2 guests for a Studio or "
            "1-Bedroom, 4 guests for a 2-Bedroom, 6 guests for a 3-Bedroom, "
            "and 8 guests for a 4-Bedroom, subject to the property's rules."
        ),
    },
    {
        "id": 19,
        "category": "Guest Requirements",
        "question": "Can I bring additional guests or visitors?",
        "answer": SHORTLET_HOUSE_RULES["visitors"],
    },
    {
        "id": 20,
        "category": "Guest Requirements",
        "question": "Can I host a party or gathering in the apartment?",
        "answer": SHORTLET_HOUSE_RULES["parties"],
    },
    {
        "id": 21,
        "category": "Guest Requirements",
        "question": "Are children allowed?",
        "answer": SHORTLET_HOUSE_RULES["children"],
    },
    {
        "id": 22,
        "category": "Guest Requirements",
        "question": "Are pets allowed?",
        "answer": SHORTLET_HOUSE_RULES["pets"],
    },

    # --------------------------------------------------------
    # HOUSE RULES
    # --------------------------------------------------------

    {
        "id": 23,
        "category": "House Rules",
        "question": "Is smoking allowed?",
        "answer": SHORTLET_HOUSE_RULES["smoking"],
    },
    {
        "id": 24,
        "category": "House Rules",
        "question": "Are parties or loud music allowed?",
        "answer": (
            "No. Parties and loud music are not permitted. Guests must avoid "
            "excessive noise or activities that disturb neighbours."
        ),
    },
    {
        "id": 25,
        "category": "House Rules",
        "question": "Can I move furniture?",
        "answer": SHORTLET_HOUSE_RULES["furniture"],
    },
    {
        "id": 26,
        "category": "House Rules",
        "question": "Can I take items outside?",
        "answer": SHORTLET_HOUSE_RULES["property_items"],
    },
    {
        "id": 27,
        "category": "House Rules",
        "question": "What if I damage something?",
        "answer": SHORTLET_HOUSE_RULES["damage"],
    },
    {
        "id": 28,
        "category": "House Rules",
        "question": "What if I lose the smart card or property?",
        "answer": SHORTLET_HOUSE_RULES["smart_card"],
    },
    {
        "id": 29,
        "category": "House Rules",
        "question": "Are photoshoots or video productions allowed?",
        "answer": SHORTLET_HOUSE_RULES["photoshoots"],
    },
    {
        "id": 30,
        "category": "House Rules",
        "question": "Are there extra charges?",
        "answer": (
            "Additional charges may apply for services or activities such as "
            "early check-in, late check-out, daily housekeeping, approved "
            "photoshoots/video productions, damages, lost smart cards, or "
            "other property-specific services."
        ),
    },
    {
        "id": 31,
        "category": "House Rules",
        "question": "What happens if I violate the rules?",
        "answer": SHORTLET_HOUSE_RULES["rule_violations"],
    },
    {
        "id": 32,
        "category": "House Rules",
        "question": "Can a guest be asked to leave?",
        "answer": (
            "Yes. Serious or repeated violations of apartment or estate "
            "rules may result in termination of the stay and the guest being "
            "required to leave, subject to the applicable terms."
        ),
    },
    {
        "id": 33,
        "category": "House Rules",
        "question": "Are estate rules required?",
        "answer": (
            "Yes. Where an apartment is located within an estate, guests are "
            "required to comply with applicable estate rules in addition to "
            "the apartment's house rules."
        ),
    },
    {
        "id": 34,
        "category": "House Rules",
        "question": "Are vehicle horns allowed?",
        "answer": SHORTLET_HOUSE_RULES["vehicle_horns"],
    },
    {
        "id": 35,
        "category": "House Rules",
        "question": "What is antisocial behaviour?",
        "answer": SHORTLET_HOUSE_RULES["antisocial_behaviour"],
    },

    # --------------------------------------------------------
    # SECURITY
    # --------------------------------------------------------

    {
        "id": 36,
        "category": "Security",
        "question": "Is the apartment or estate secured?",
        "answer": SHORTLET_HOUSE_RULES["security"],
    },
    {
        "id": 37,
        "category": "Security",
        "question": "Is there 24/7 security?",
        "answer": (
            "Where provided, estates may have 24/7 security personnel. "
            "Guests should confirm the specific security arrangements of "
            "the property before booking."
        ),
    },
    {
        "id": 38,
        "category": "Security",
        "question": "Does the property have CCTV?",
        "answer": (
            "CCTV may be available in common or estate areas where provided. "
            "Coverage varies by property."
        ),
    },
    {
        "id": 39,
        "category": "Parking",
        "question": "Is parking available?",
        "answer": (
            "Parking availability depends on the property or estate. "
            "Guests should confirm parking arrangements before booking."
        ),
    },
    {
        "id": 40,
        "category": "Parking",
        "question": "What are the parking rules?",
        "answer": (
            "Guests must follow all parking instructions provided by the "
            "property or estate, including designated parking spaces and "
            "security requirements."
        ),
    },
    {
        "id": 41,
        "category": "Security",
        "question": "What if I notice damage on arrival?",
        "answer": (
            "Report it to the host, manager, or designated property contact "
            "as soon as possible, preferably before using the affected item "
            "or area."
        ),
    },
    {
        "id": 42,
        "category": "Security",
        "question": "Who is responsible for children?",
        "answer": (
            "Parents or guardians are responsible for supervising children "
            "and ensuring their safety throughout the stay."
        ),
    },

    # --------------------------------------------------------
    # CAUTION / SECURITY DEPOSIT
    # --------------------------------------------------------

    {
        "id": 43,
        "category": "Caution Fee",
        "question": "Is a caution or security deposit required?",
        "answer": (
            "Some properties require a refundable caution/security deposit. "
            "The amount and conditions vary by property."
        ),
    },
    {
        "id": 44,
        "category": "Caution Fee",
        "question": "When is the caution deposit paid?",
        "answer": (
            "Where required, the caution/security deposit is normally paid "
            "before or at check-in according to the property's booking terms."
        ),
    },
    {
        "id": 45,
        "category": "Caution Fee",
        "question": "When is the caution deposit refunded?",
        "answer": SHORTLET_HOUSE_RULES["deposit_refund"],
    },
    {
        "id": 46,
        "category": "Caution Fee",
        "question": "What can be deducted from the deposit?",
        "answer": (
            "Applicable deductions may include damage, missing items, lost "
            "smart cards, excessive cleaning, unpaid charges, or penalties "
            "arising from applicable house or estate rules."
        ),
    },
    {
        "id": 47,
        "category": "Caution Fee",
        "question": "What if damage exceeds the deposit?",
        "answer": (
            "If verified damage or other outstanding charges exceed the "
            "caution/security deposit, the guest may be required to pay the "
            "remaining balance."
        ),
    },
    {
        "id": 48,
        "category": "Caution Fee",
        "question": "Can the deposit be forfeited for rule violations?",
        "answer": (
            "Yes. Where permitted by the applicable terms, serious house or "
            "estate-rule violations may result in partial or full forfeiture "
            "of the caution/security deposit."
        ),
    },

    # --------------------------------------------------------
    # HOUSEKEEPING / FACILITIES
    # --------------------------------------------------------

    {
        "id": 49,
        "category": "Housekeeping",
        "question": "How often is housekeeping provided?",
        "answer": SHORTLET_HOUSE_RULES["housekeeping"],
    },
    {
        "id": 50,
        "category": "Housekeeping",
        "question": "Is daily housekeeping available?",
        "answer": (
            "Daily housekeeping may be available depending on the property."
        ),
    },
    {
        "id": 51,
        "category": "Housekeeping",
        "question": "Is there an additional charge for daily housekeeping?",
        "answer": SHORTLET_HOUSE_RULES["daily_housekeeping"],
    },
    {
        "id": 52,
        "category": "Housekeeping",
        "question": "What time does housekeeping take place?",
        "answer": (
            "Housekeeping is generally carried out between 9:00 a.m. and "
            "2:00 p.m., subject to the property's arrangements."
        ),
    },
    {
        "id": 53,
        "category": "Facilities",
        "question": "Is there a swimming pool?",
        "answer": (
            "Some properties have swimming pools. Availability must be "
            "confirmed for the specific apartment."
        ),
    },
    {
        "id": 54,
        "category": "Facilities",
        "question": "What are the swimming pool operating hours?",
        "answer": SHORTLET_HOUSE_RULES["pool"],
    },
    {
        "id": 55,
        "category": "Facilities",
        "question": "What are the swimming pool safety rules?",
        "answer": SHORTLET_HOUSE_RULES["pool_safety"],
    },
    {
        "id": 56,
        "category": "Guest Support",
        "question": "Who can assist me during my stay?",
        "answer": (
            "Guests should use the contact provided by the host, manager, "
            "booking provider, or property representative for assistance "
            "during their stay."
        ),
    },
]


# ============================================================
# CAR HIRE FAQ
# ============================================================

CAR_HIRE_FAQ = [

    {
        "id": 57,
        "category": "Car Hire",
        "question": "Do you provide car hire for short-let guests?",
        "answer": (
            "Yes, where available, guests may request car-hire or "
            "transportation services alongside their short-let booking. "
            "Availability depends on the service provider."
        ),
    },
    {
        "id": 58,
        "category": "Car Hire",
        "question": "What types of cars are available?",
        "answer": (
            "Vehicle options may include economy, saloon, SUV, executive, "
            "luxury, or other categories depending on availability."
        ),
    },
    {
        "id": 59,
        "category": "Car Hire",
        "question": "Can I hire a car for my entire stay?",
        "answer": (
            "Yes, where available, vehicles can be hired for the duration of "
            "your stay subject to the provider's rental terms."
        ),
    },
    {
        "id": 60,
        "category": "Car Hire",
        "question": "Can I hire a car for a few hours or one day?",
        "answer": (
            "Short-duration rentals may be available, depending on the "
            "vehicle provider and rental terms."
        ),
    },
    {
        "id": 61,
        "category": "Car Hire",
        "question": "Can I book a car before arriving in Lagos?",
        "answer": (
            "Yes, advance requests can be made where the provider accepts "
            "pre-arrival bookings."
        ),
    },
    {
        "id": 62,
        "category": "Car Hire",
        "question": "Can I book a car together with my short-let?",
        "answer": (
            "Yes. Where available, short-let accommodation and car-hire "
            "services can be requested together."
        ),
    },
    {
        "id": 63,
        "category": "Car Hire",
        "question": "Is airport pickup or drop-off available?",
        "answer": (
            "Airport pickup and drop-off may be available depending on the "
            "vehicle provider and requested airport transfer."
        ),
    },
    {
        "id": 64,
        "category": "Car Hire",
        "question": "Can I hire a driver or chauffeur?",
        "answer": (
            "Yes, chauffeur-driven vehicles may be available depending on "
            "the provider and vehicle category."
        ),
    },
    {
        "id": 65,
        "category": "Car Hire",
        "question": "Is self-drive available?",
        "answer": (
            "Self-drive may be available for eligible renters and vehicles, "
            "subject to the provider's requirements."
        ),
    },
    {
        "id": 66,
        "category": "Car Hire",
        "question": "What are the requirements for car hire?",
        "answer": (
            "Requirements vary by provider and may include valid "
            "identification, a valid driver's licence for self-drive, "
            "contact information, and other rental documentation."
        ),
    },
    {
        "id": 67,
        "category": "Car Hire",
        "question": "Is a security deposit required for car hire?",
        "answer": (
            "Some vehicle providers require a refundable security deposit. "
            "The amount and refund conditions depend on the rental provider."
        ),
    },
    {
        "id": 68,
        "category": "Car Hire",
        "question": "What is included in the car-hire price?",
        "answer": (
            "Inclusions vary. Depending on the provider, the price may cover "
            "the vehicle, driver, agreed rental period, or specific services. "
            "Always confirm inclusions before payment."
        ),
    },
    {
        "id": 69,
        "category": "Car Hire",
        "question": "Is fuel included?",
        "answer": (
            "Fuel is not automatically assumed to be included. Confirm the "
            "fuel arrangement with the vehicle provider."
        ),
    },
    {
        "id": 70,
        "category": "Car Hire",
        "question": "Are tolls and parking included?",
        "answer": (
            "Tolls, parking, airport fees, and similar charges may be "
            "additional unless the provider specifically states that they "
            "are included."
        ),
    },
    {
        "id": 71,
        "category": "Car Hire",
        "question": "Is insurance included?",
        "answer": (
            "Insurance coverage depends on the vehicle provider and rental "
            "agreement. Confirm the type and limits of coverage before "
            "accepting the vehicle."
        ),
    },
    {
        "id": 72,
        "category": "Car Hire",
        "question": "Can I travel outside Lagos with the rental car?",
        "answer": (
            "Travel outside Lagos may be possible with prior approval from "
            "the vehicle provider. Additional charges or restrictions may "
            "apply."
        ),
    },
    {
        "id": 73,
        "category": "Car Hire",
        "question": "Can I extend my car rental?",
        "answer": (
            "Extensions may be possible subject to vehicle availability and "
            "provider approval."
        ),
    },
    {
        "id": 74,
        "category": "Car Hire",
        "question": "What happens if I return the vehicle late?",
        "answer": (
            "Late returns may attract additional charges according to the "
            "vehicle provider's rental agreement."
        ),
    },
    {
        "id": 75,
        "category": "Car Hire",
        "question": "What happens if the vehicle is damaged?",
        "answer": (
            "The renter may be responsible for applicable damage costs "
            "according to the rental agreement, insurance arrangements, and "
            "the circumstances of the damage."
        ),
    },
    {
        "id": 76,
        "category": "Car Hire",
        "question": "What if I lose the car keys or documents?",
        "answer": (
            "Loss of keys, vehicle documents, or other supplied items may "
            "result in replacement or administrative charges."
        ),
    },
    {
        "id": 77,
        "category": "Car Hire",
        "question": "Can I cancel my car rental?",
        "answer": (
            "Cancellation terms depend on the vehicle provider and booking "
            "agreement."
        ),
    },
    {
        "id": 78,
        "category": "Car Hire",
        "question": "Can I request a specific vehicle?",
        "answer": (
            "You may request a specific vehicle or vehicle category, but "
            "confirmation depends on availability."
        ),
    },
    {
        "id": 79,
        "category": "Car Hire",
        "question": "Are luxury or executive vehicles available?",
        "answer": (
            "Luxury and executive vehicles may be available depending on "
            "the provider's fleet."
        ),
    },
    {
        "id": 80,
        "category": "Car Hire",
        "question": "Can I hire a vehicle for business, events, or tours?",
        "answer": (
            "Yes, where available, vehicles may be arranged for business "
            "travel, events, airport transfers, sightseeing, tours, and "
            "other approved purposes."
        ),
    },
    {
        "id": 81,
        "category": "Car Hire",
        "question": "Can I hire a vehicle for multiple guests?",
        "answer": (
            "Yes, vehicle selection should be based on the number of "
            "passengers and luggage. The appropriate vehicle category must "
            "be confirmed before booking."
        ),
    },
    {
        "id": 82,
        "category": "Car Hire",
        "question": "Can I book airport transfer only?",
        "answer": (
            "Yes, airport pickup or drop-off may be booked separately where "
            "the transportation provider offers airport-transfer services."
        ),
    },
    {
        "id": 83,
        "category": "Car Hire",
        "question": "How do I contact the car-hire provider?",
        "answer": (
            "The contact details of the relevant vehicle provider should be "
            "provided as part of the confirmed booking or service arrangement."
        ),
    },
]


# ============================================================
# COMBINED SHORT-LET + CAR HIRE FAQ
# ============================================================

COMBINED_SERVICE_FAQ = [

    {
        "id": 84,
        "category": "Combined Services",
        "question": "Can I book a shortlet apartment and car hire service together?",
        "answer": (
            "Yes. Where available, guests can request both short-let "
            "accommodation and car-hire services as part of their stay. "
            "This can simplify accommodation, airport transfers, and "
            "transportation planning. Availability, vehicle type, driver "
            "options, pricing, and terms depend on the provider."
        ),
    },

    {
        "id": 85,
        "category": "Combined Services",
        "question": "Can I arrange airport pickup with my short-let booking?",
        "answer": (
            "Yes, where airport-transfer services are available. Guests may "
            "request airport pickup or drop-off alongside their accommodation "
            "booking."
        ),
    },
]


# ============================================================
# VERIFIED AGENTS AND HOMES FAQ
# ============================================================

VERIFICATION_FAQ = [

    {
        "id": 86,
        "category": "About VAH",
        "question": "What is Verified Agents and Homes Ltd?",
        "answer": (
            "Verified Agents and Homes Ltd is a property and real-estate "
            "verification service designed to help customers make safer "
            "property and accommodation decisions before making transactions."
        ),
    },

    {
        "id": 87,
        "category": "About VAH",
        "question": "What is the VAH Database?",
        "answer": (
            "The VAH Database is a verification information system used to "
            "record and organize available information relating to properties, "
            "agents, documents, short-let addresses, owners, managers, and "
            "verification updates."
        ),
    },

    {
        "id": 88,
        "category": "Payment Safety",
        "question": "Why should I verify before payment?",
        "answer": (
            "Verification can help identify inconsistencies, missing "
            "information, questionable documentation, identity concerns, or "
            "other warning signs before money changes hands."
        ),
    },

    {
        "id": 89,
        "category": "Agent Verification",
        "question": "How can I verify a real-estate agent?",
        "answer": (
            "You can request an agent search or verification using available "
            "identifying information such as the agent's name, phone number, "
            "agency name, or VAH verification number."
        ),
    },

    {
        "id": 90,
        "category": "Agent Verification",
        "question": "Can VAH verify the owner or manager of a property?",
        "answer": (
            "Yes, where sufficient information is available, VAH can support "
            "verification of a property owner or short-let manager."
        ),
    },

    {
        "id": 91,
        "category": "Property Verification",
        "question": "Can VAH verify land or house documents?",
        "answer": (
            "Yes. VAH can assist with property and document verification "
            "based on the documents and information available for review."
        ),
    },

    {
        "id": 92,
        "category": "Document Verification",
        "question": "What types of documents can be verified?",
        "answer": (
            "Depending on the property and available records, documents may "
            "include title documents, deeds, surveys, Certificates of "
            "Occupancy, approved building plans, building approvals, and "
            "other relevant property documentation."
        ),
    },

    {
        "id": 93,
        "category": "Property Verification",
        "question": "Can VAH verify whether a property listing is genuine?",
        "answer": (
            "VAH can conduct available verification checks on the property, "
            "agent, owner, manager, address, and documents. Verification "
            "should be treated as due-diligence information rather than an "
            "absolute guarantee."
        ),
    },

    {
        "id": 94,
        "category": "Short-let Verification",
        "question": "Can VAH verify a short-let apartment?",
        "answer": (
            "Yes. Available checks may include the short-let address, owner, "
            "manager, property information, and reported concerns."
        ),
    },

    {
        "id": 95,
        "category": "Verification Number",
        "question": "What is a VAH Verification Number?",
        "answer": (
            "A VAH Verification Number is a reference associated with a "
            "verification record. It can help customers identify and check "
            "the relevant verification information."
        ),
    },

    {
        "id": 96,
        "category": "Verification Number",
        "question": "How do I check a VAH Verification Number?",
        "answer": (
            "Provide or search the verification number through the applicable "
            "VAH verification/database service and compare the returned "
            "information with the property, agent, owner, or manager details "
            "you are dealing with."
        ),
    },

    {
        "id": 97,
        "category": "Verification Number",
        "question": "Does a VAH Verification Number guarantee my safety?",
        "answer": (
            "No. A verification number does not guarantee that a transaction "
            "will be completely safe or that no future dispute, fraud, loss, "
            "property defect, or service problem can occur. It is a "
            "due-diligence reference."
        ),
    },

    {
        "id": 98,
        "category": "Verification Updates",
        "question": "How often is verification information updated?",
        "answer": (
            "Verification information may be updated periodically as new "
            "information becomes available. Customers should check the "
            "latest available record before making payment."
        ),
    },

    {
        "id": 99,
        "category": "Location Verification",
        "question": "Can VAH verify a property address or location?",
        "answer": (
            "VAH can assist with available address and location checks. "
            "Customers should compare the verified information with the "
            "actual property and transaction details."
        ),
    },

    {
        "id": 100,
        "category": "Fraud Prevention",
        "question": "What if an agent refuses to provide a verification number?",
        "answer": (
            "A refusal should be treated as a reason to exercise caution. "
            "Customers should independently verify the agent, property, "
            "documents, and payment instructions before proceeding."
        ),
    },

    {
        "id": 101,
        "category": "Reporting",
        "question": "How can I report suspected fraud or a verification concern?",
        "answer": (
            "Use the applicable VAH reporting channel and provide as much "
            "relevant information as possible, including names, phone "
            "numbers, property details, documents, payment information, "
            "screenshots, and the nature of the concern. Do not share "
            "unnecessary passwords or sensitive credentials."
        ),
    },

    {
        "id": 102,
        "category": "Reporting",
        "question": "What happens after I report a concern?",
        "answer": (
            "The reported information can be reviewed and recorded for "
            "further investigation or verification. A report does not "
            "automatically establish that fraud has occurred."
        ),
    },

    {
        "id": 103,
        "category": "Ownership",
        "question": "Can VAH verify property ownership?",
        "answer": (
            "VAH can conduct available ownership-related checks based on "
            "documents, records, and information available for verification."
        ),
    },

    {
        "id": 104,
        "category": "Property Verification",
        "question": "Should I verify before paying for land or a house?",
        "answer": (
            "Yes. Customers are strongly encouraged to conduct appropriate "
            "property, ownership, document, location, agent, and transaction "
            "due diligence before making payment."
        ),
    },

    {
        "id": 105,
        "category": "Investor Due Diligence",
        "question": "Can investors use VAH for property due diligence?",
        "answer": (
            "Yes. Investors can use available VAH verification services as "
            "part of a broader due-diligence process before committing funds."
        ),
    },

    {
        "id": 106,
        "category": "Tourists and Guests",
        "question": "Can tourists and short-let guests use VAH?",
        "answer": (
            "Yes. Tourists, visitors, tenants, and short-let guests can use "
            "available verification services to support checks on short-let "
            "addresses, owners, managers, agents, and other relevant details."
        ),
    },

    {
        "id": 107,
        "category": "Registration",
        "question": "Can property owners or agents register with VAH?",
        "answer": (
            "Property owners, agents, and relevant property representatives "
            "may request registration or verification where the applicable "
            "VAH service is available."
        ),
    },

    {
        "id": 108,
        "category": "Verification Request",
        "question": "How do I request a verification?",
        "answer": (
            "Submit the relevant property, agent, owner, manager, or document "
            "information through the applicable VAH verification channel."
        ),
    },

    {
        "id": 109,
        "category": "Verification Request",
        "question": "What information is required for verification?",
        "answer": (
            "Requirements vary by verification type but may include property "
            "address, property reference, agent details, owner/manager "
            "details, phone number, relevant documents, and other information "
            "needed for the requested check."
        ),
    },

    {
        "id": 110,
        "category": "Verification Fees",
        "question": "How much does verification cost?",
        "answer": (
            "Verification fees depend on the type and scope of service "
            "requested. Customers should confirm the current applicable fee "
            "before payment."
        ),
    },

    {
        "id": 111,
        "category": "Verification Time",
        "question": "How long does verification take?",
        "answer": (
            "Processing time depends on the type of verification, availability "
            "of records, completeness of submitted information, and any "
            "required external confirmation."
        ),
    },

    {
        "id": 112,
        "category": "Verification Disclaimer",
        "question": "Does verification guarantee that I will not lose money?",
        "answer": (
            "No. Verification reduces information gaps and may identify "
            "warning signs, but it cannot guarantee that a customer will "
            "never experience fraud, loss, disputes, property defects, or "
            "other transaction problems."
        ),
    },

    {
        "id": 113,
        "category": "Verification",
        "question": "What is the difference between property verification and document verification?",
        "answer": (
            "Property verification considers available information about the "
            "property, address, ownership, agent, owner, manager, or listing. "
            "Document verification focuses specifically on reviewing and "
            "checking relevant property documents and their available records."
        ),
    },

    {
        "id": 114,
        "category": "Payment Safety",
        "question": "Why should I verify before payment?",
        "answer": PAYMENT_SAFETY_NOTICE,
    },
]


# ============================================================
# FAQ COLLECTION
# ============================================================

FAQ_SECTIONS = {
    "shortlet": SHORTLET_FAQ,
    "car_hire": CAR_HIRE_FAQ,
    "combined_services": COMBINED_SERVICE_FAQ,
    "verification": VERIFICATION_FAQ,
}


# ============================================================
# FAQ HELPER FUNCTIONS
# ============================================================

def get_shortlet_faq():
    """
    Return all short-let FAQs.
    """
    return SHORTLET_FAQ


def get_car_hire_faq():
    """
    Return all car-hire FAQs.
    """
    return CAR_HIRE_FAQ


def get_verification_faq():
    """
    Return all Verified Agents and Homes verification FAQs.
    """
    return VERIFICATION_FAQ


def get_shortlet_house_rules():
    """
    Return the current short-let house rules.
    """
    return SHORTLET_HOUSE_RULES


def get_combined_booking_faq():
    """
    Return FAQs covering combined short-let and car-hire services.
    """
    return COMBINED_SERVICE_FAQ


def get_payment_safety_guidance():
    """
    Return payment and transaction safety guidance.
    """
    return PAYMENT_SAFETY_NOTICE


def get_all_faqs():
    """
    Return every FAQ grouped by category.
    """
    return FAQ_SECTIONS


def search_faq(query, section=None, limit=5):
    """
    Search the FAQ database using simple keyword matching.

    Parameters:
        query (str): User's question or search phrase.
        section (str|None): Optional section:
            'shortlet'
            'car_hire'
            'combined_services'
            'verification'
        limit (int): Maximum number of results.

    Returns:
        list: Matching FAQ records.
    """

    if not query:
        return []

    query_words = {
        word.strip(".,?!:;()[]{}").lower()
        for word in str(query).split()
        if len(word.strip(".,?!:;()[]{}")) > 2
    }

    if section:
        faq_source = FAQ_SECTIONS.get(section, [])
    else:
        faq_source = (
            SHORTLET_FAQ
            + CAR_HIRE_FAQ
            + COMBINED_SERVICE_FAQ
            + VERIFICATION_FAQ
        )

    results = []

    for faq in faq_source:
        searchable_text = (
            f"{faq.get('question', '')} "
            f"{faq.get('answer', '')} "
            f"{faq.get('category', '')}"
        ).lower()

        score = sum(
            1 for word in query_words
            if word in searchable_text
        )

        if score > 0:
            result = dict(faq)
            result["_score"] = score
            results.append(result)

    results.sort(key=lambda item: item["_score"], reverse=True)

    for result in results:
        result.pop("_score", None)

    return results[:limit]


def get_faq_answer(question, section=None):
    """
    Return the best FAQ answer for a question.

    This performs a simple keyword search and returns the best match.
    """
    results = search_faq(
        query=question,
        section=section,
        limit=1,
    )

    if not results:
        return None

    return results[0]


def get_faq_categories(section=None):
    """
    Return the FAQ categories available in a section.
    """

    if section:
        faq_source = FAQ_SECTIONS.get(section, [])
    else:
        faq_source = (
            SHORTLET_FAQ
            + CAR_HIRE_FAQ
            + COMBINED_SERVICE_FAQ
            + VERIFICATION_FAQ
        )

    return sorted({
        faq["category"]
        for faq in faq_source
        if faq.get("category")
    })
# ============================================================
# JAHZ EMPIRE HOTEL & SUITES
# HOTEL INFORMATION, SERVICES, FAQ & SEARCH
# ============================================================


# ============================================================
# JAHZ HOTEL INFORMATION
# ============================================================

JAHZ_HOTEL_INFORMATION = {
    "name": "JAHZ Empire Hotel & Suites",

    "address": (
        "14 Gbadamosi Alomaja Street, "
        "Kingdom Hall Bus Stop, Abijo, "
        "Lekki-Epe Expressway, Lagos."
    ),

    "phone": [
        "+234 706 275 4478",
        "+234 806 951 9327",
    ],

    "email": "info@jahzempiresuites.com",

    "room_categories": {
        "classic": (
            "Classic: 1-Bedroom with kitchenette."
        ),
        "deluxe": (
            "Deluxe: 1-Bedroom with spa bathtub."
        ),
        "executive": (
            "Executive: 2-Bedrooms with kitchenette."
        ),
    },
}


# ============================================================
# JAHZ HOTEL SERVICES
# ============================================================

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

    "payment": {
        "name": "Payment",
        "description": (
            "JAHZ Empire Suites & Resort does NOT accept cash payments. "
            "All payments must be made only into the official JAHZ Empire "
            "Suites & Resort account using payment details provided or "
            "confirmed by the hotel. Customers should not send money to "
            "personal accounts or unverified third parties."
        ),
    },
}


# ============================================================
# HOTEL INFORMATION FUNCTIONS
# ============================================================

def get_jahz_hotel_information():
    """Return official information about JAHZ Empire Hotel & Suites."""

    phone_numbers = ", ".join(
        JAHZ_HOTEL_INFORMATION["phone"]
    )

    rooms = JAHZ_HOTEL_INFORMATION["room_categories"]

    return (
        "JAHZ Empire Hotel & Suites\n\n"
        f"Address: {JAHZ_HOTEL_INFORMATION['address']}\n"
        f"Phone: {phone_numbers}\n"
        f"Email: {JAHZ_HOTEL_INFORMATION['email']}\n\n"
        "Room Categories:\n"
        f"- {rooms['classic']}\n"
        f"- {rooms['deluxe']}\n"
        f"- {rooms['executive']}"
    )


def get_jahz_room_categories():
    """Return the official JAHZ Empire Hotel & Suites room categories."""

    rooms = JAHZ_HOTEL_INFORMATION["room_categories"]

    return (
        "JAHZ Empire Hotel & Suites\n"
        "Room Categories\n\n"
        f"- {rooms['classic']}\n"
        f"- {rooms['deluxe']}\n"
        f"- {rooms['executive']}"
    )


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

    if not service:
        return (
            "Please provide the hotel service you want information about."
        )

    search_term = str(service).strip().lower()

    if not search_term:
        return (
            "Please provide the hotel service you want information about."
        )

    for service_data in JAHZ_HOTEL_SERVICES.values():

        name = service_data["name"].lower()
        description = service_data["description"].lower()

        if (
            search_term in name
            or search_term in description
        ):
            return (
                "JAHZ Empire Hotel & Suites\n"
                f"Service: {service_data['name']}\n"
                f"Description: {service_data['description']}"
            )

    return (
        "No JAHZ Empire Hotel & Suites service was found "
        f"matching '{service}'."
    )


def get_jahz_hotel_payment_policy():
    """Return the official JAHZ payment policy."""

    return (
        "JAHZ Empire Suites & Resort Payment Policy\n\n"
        "JAHZ Empire Suites & Resort does NOT accept cash payments.\n\n"
        "All payments must be made only into the official "
        "JAHZ Empire Suites & Resort account using payment details "
        "provided or confirmed by the hotel.\n\n"
        "Customers should NOT send money to personal accounts or "
        "unverified third parties.\n\n"
        "If you are unsure about payment details, contact the hotel "
        "directly and confirm the official payment information before "
        "making any payment."
    )


# ============================================================
# HOTEL SERVICE RECOMMENDATION
# ============================================================

def recommend_jahz_hotel_service(request):
    """Identify the JAHZ hotel service that best matches a customer request."""

    if not request:
        return "Please describe what you need help with."

    request_lower = str(request).strip().lower()

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
            "classic",
            "deluxe",
            "delux",
            "executive",
            "bedroom",
            "kitchenette",
            "spa bathtub",
        ],

        "room_booking": [
            "book a room",
            "book room",
            "room booking",
            "reserve a room",
            "reservation",
            "hotel booking",
            "book accommodation",
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

        "payment": [
            "payment",
            "pay",
            "paying",
            "cash",
            "bank",
            "account",
            "payment details",
            "where do i pay",
            "how do i pay",
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
            "I can help with JAHZ Empire Hotel & Suites services and "
            "facilities. Please tell me what you need, such as a room "
            "booking, event, gym, swimming pool, membership, "
            "short-let accommodation, Air Peace flight, or payment "
            "information."
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


# ============================================================
# CUSTOMER ENQUIRY
# ============================================================

def create_jahz_hotel_enquiry(customer_request):
    """Prepare a JAHZ hotel customer enquiry for human follow-up."""

    if not customer_request:
        return (
            "No customer request was provided. "
            "Please provide the customer's request."
        )

    request = str(customer_request).strip()

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


# ============================================================
# JAHZ EMPIRE SUITES & RESORT
# HOTEL FAQ
# ============================================================

JAHZ_HOTEL_FAQ = {

    # --------------------------------------------------------
    # RESERVATIONS & ROOM BOOKING
    # --------------------------------------------------------

    "how_can_i_make_a_room_reservation": {
        "question": "How can I make a room reservation?",
        "answer": (
            "Guests can make a room reservation through the official hotel "
            "website, by contacting the reservations team directly, or through "
            "an official booking channel provided by JAHZ Empire Suites & Resort. "
            "Guests may be required to provide their preferred room type, "
            "check-in and check-out dates, number of guests, and contact details."
        )
    },

    "booking_information": {
        "question": "What information do I need to provide when booking a room?",
        "answer": (
            "Guests will generally need to provide their full name, contact "
            "details, preferred check-in and check-out dates, number of guests, "
            "preferred room type, and any special requirements. Additional "
            "information may be requested depending on the reservation."
        )
    },

    "booking_for_another_person": {
        "question": "Can I reserve a room for another person?",
        "answer": (
            "Yes. A guest may make a reservation on behalf of another person. "
            "The person staying at the hotel must meet the hotel's identification "
            "and check-in requirements when they arrive."
        )
    },

    "specific_room_request": {
        "question": "Can I request a particular room or room location?",
        "answer": (
            "Yes. Guests may request preferences such as a particular floor, "
            "room location, bed configuration, or other available features. "
            "Requests are subject to availability and are not guaranteed until "
            "confirmed by the hotel."
        )
    },

    "group_room_booking": {
        "question": "Can I book multiple rooms for a group?",
        "answer": (
            "Yes. Group bookings can be arranged for families, companies, "
            "wedding guests, tour groups, conferences, and other occasions. "
            "Larger reservations may have different payment, cancellation, "
            "and booking conditions."
        )
    },

    "extend_stay": {
        "question": "Can I extend my stay after checking in?",
        "answer": (
            "Yes, subject to room availability. Guests who wish to extend "
            "their stay should contact the front desk or reservations team "
            "as early as possible so availability and the applicable rate "
            "can be confirmed."
        )
    },

    "early_arrival": {
        "question": "What happens if I arrive before my check-in time?",
        "answer": (
            "Early arrival does not automatically guarantee immediate access "
            "to the room. If the room is ready, early check-in may be possible. "
            "Otherwise, the hotel may be able to assist with luggage storage "
            "while the guest waits."
        )
    },

    "late_arrival": {
        "question": "What happens if I arrive late at night?",
        "answer": (
            "Guests expecting to arrive late should inform the hotel in advance. "
            "This allows the reservations or front-desk team to make the "
            "necessary arrangements for the guest's arrival."
        )
    },


    # --------------------------------------------------------
    # CHECK-IN, CHECK-OUT & GUEST POLICIES
    # --------------------------------------------------------

    "check_in_time": {
        "question": "What time is check-in?",
        "answer": (
            "The standard check-in time is based on the hotel's current policy "
            "and should be confirmed with the reservations team or stated on "
            "the guest's booking confirmation. Early check-in may be available "
            "depending on room readiness."
        )
    },

    "check_out_time": {
        "question": "What time is check-out?",
        "answer": (
            "The standard check-out time is stated on the guest's booking "
            "confirmation. Guests who require additional time should request "
            "late check-out in advance. Late check-out is subject to availability "
            "and may attract an additional charge."
        )
    },

    "check_in_requirements": {
        "question": "What do I need to check in at the hotel?",
        "answer": (
            "Guests are normally required to provide a valid form of "
            "identification and their reservation details or confirmation. "
            "Additional requirements may apply depending on the booking."
        )
    },

    "hotel_visitors": {
        "question": "Can someone visit me in my hotel room?",
        "answer": (
            "Visitors may be permitted subject to the hotel's visitor and "
            "security policies. Visitors may be required to register at the "
            "front desk and comply with the hotel's visiting requirements."
        )
    },

    "overnight_guest": {
        "question": "Can an unregistered person stay overnight in my room?",
        "answer": (
            "Overnight guests must comply with the hotel's occupancy and "
            "registration policies. Guests who intend to have another person "
            "stay overnight should inform the hotel so the appropriate "
            "arrangements can be made."
        )
    },

    "luggage_storage": {
        "question": "Can I leave my luggage at the hotel before check-in or after check-out?",
        "answer": (
            "Luggage storage may be available depending on the hotel's "
            "facilities and policies. Guests should contact the front desk "
            "to confirm the available arrangements."
        )
    },

    "lost_property": {
        "question": "What should I do if I leave something behind in my room?",
        "answer": (
            "Guests should contact the hotel as soon as possible and provide "
            "details about the missing item, room, and dates of stay. The hotel "
            "can check its lost-and-found records and advise the guest about "
            "collection or other available arrangements."
        )
    },


    # --------------------------------------------------------
    # PAYMENTS, RATES & CANCELLATION
    # --------------------------------------------------------

    "payment_methods": {
        "question": "How do I pay for my hotel booking?",
        "answer": (
            "JAHZ Empire Suites & Resort does NOT accept cash payments for "
            "hotel bookings. All payments must be made only into the official "
            "JAHZ Empire Suites & Resort account through the payment method "
            "provided or confirmed by the hotel. Guests should confirm the "
            "official payment details with the hotel before making any payment."
        )
    },

    "cash_payment": {
        "question": "Can I pay cash at the hotel?",
        "answer": (
            "No. JAHZ Empire Suites & Resort does not accept cash payments. "
            "All payments must be made only into the official JAHZ Empire "
            "Suites & Resort account using the official payment details "
            "provided or confirmed by the hotel."
        )
    },

    "payment_security": {
        "question": "How can I make sure I am paying into the correct account?",
        "answer": (
            "Guests should only make payments using official payment details "
            "provided or confirmed directly by JAHZ Empire Suites & Resort. "
            "Do not send money to a personal account or an account provided "
            "by an unverified third party. When in doubt, contact the hotel "
            "directly before making payment."
        )
    },

    "room_price_includes": {
        "question": "Does the room price include all hotel charges?",
        "answer": (
            "The total price depends on the specific booking. Some rates may "
            "include certain services or benefits, while additional services "
            "may attract separate charges. Guests should review their booking "
            "details and quotation before making payment."
        )
    },

    "room_rates": {
        "question": "Do room rates change?",
        "answer": (
            "Yes. Room rates may vary according to the room category, dates, "
            "length of stay, demand, special offers, holidays, and other "
            "applicable factors."
        )
    },

    "deposit": {
        "question": "Is a deposit required to reserve a room?",
        "answer": (
            "Some reservations may require an advance payment or deposit. "
            "The amount and payment deadline depend on the hotel's booking "
            "terms and the type of reservation."
        )
    },

    "cancel_reservation": {
        "question": "Can I cancel my reservation?",
        "answer": (
            "Cancellation may be permitted depending on the reservation's "
            "terms and conditions. Cancellation fees or non-refundable "
            "conditions may apply to certain bookings. Guests should review "
            "the cancellation policy before confirming their reservation."
        )
    },

    "change_reservation": {
        "question": "Can I change my reservation after booking?",
        "answer": (
            "Reservation changes may be possible depending on availability "
            "and the booking conditions. Changes to dates, room types, number "
            "of guests, or length of stay may affect the total price."
        )
    },

    "no_show": {
        "question": "What happens if I do not arrive for my reservation?",
        "answer": (
            "A reservation that is not used without prior notice may be "
            "treated as a no-show. Depending on the booking terms, the hotel "
            "may apply a no-show charge or retain an applicable advance payment."
        )
    },

    "refund": {
        "question": "Can I get a refund if I cancel my booking?",
        "answer": (
            "Refund eligibility depends on the cancellation policy and the "
            "terms of the specific reservation. Non-refundable bookings may "
            "not qualify for a refund."
        )
    },


    # --------------------------------------------------------
    # ROOMS & ACCOMMODATION
    # --------------------------------------------------------

    "room_types": {
        "question": "What types of rooms and suites are available?",
        "answer": (
            "JAHZ Empire Suites & Resort offers different room and suite "
            "categories. Current categories include Classic, Deluxe, and "
            "Executive. Guests can contact the hotel for current availability "
            "and applicable rates."
        )
    },

    "room_occupancy": {
        "question": "How many people can stay in one room?",
        "answer": (
            "Occupancy depends on the room category and the hotel's approved "
            "capacity. Guests should provide the correct number of occupants "
            "when booking so that an appropriate room can be assigned."
        )
    },

    "family_rooms": {
        "question": "Are rooms suitable for families?",
        "answer": (
            "Selected rooms may be suitable for families depending on their "
            "size and sleeping arrangements. Families should provide the "
            "number and ages of guests when making a reservation."
        )
    },

    "extra_bed": {
        "question": "Are extra beds or additional sleeping arrangements available?",
        "answer": (
            "Extra beds or additional sleeping arrangements may be available "
            "for selected room categories. Availability should be confirmed "
            "before booking because not every room can accommodate an additional bed."
        )
    },

    "bed_configuration": {
        "question": "Can I request a particular bed arrangement?",
        "answer": (
            "Guests may request available bed configurations such as a "
            "king-size bed or double beds. Requests depend on the selected "
            "room category and availability."
        )
    },

    "housekeeping": {
        "question": "Are rooms cleaned every day?",
        "answer": (
            "Housekeeping services are provided according to the hotel's "
            "housekeeping schedule and policies. Guests may contact the front "
            "desk regarding cleaning preferences or additional housekeeping needs."
        )
    },

    "room_problem": {
        "question": "What should I do if I have a problem with my room?",
        "answer": (
            "Guests should report room problems to the front desk or hotel "
            "management as soon as possible. The hotel team will investigate "
            "the issue and, where possible, arrange a repair, replacement, "
            "or alternative solution."
        )
    },


    # --------------------------------------------------------
    # HOTEL FACILITIES & SERVICES
    # --------------------------------------------------------

    "wifi": {
        "question": "Does the hotel provide Wi-Fi?",
        "answer": (
            "Wi-Fi availability and access details depend on the hotel's "
            "current facilities. Guests can request the Wi-Fi access information "
            "from the front desk and report any connection problems for assistance."
        )
    },

    "restaurant": {
        "question": "Does the hotel have a restaurant or dining facility?",
        "answer": (
            "Guests can enquire about the hotel's current restaurant and "
            "dining services, including available meals, operating hours, "
            "menus, reservations, and payment arrangements."
        )
    },

    "room_service": {
        "question": "Does the hotel offer room service?",
        "answer": (
            "Room service availability depends on the hotel's current services "
            "and operating hours. Guests should contact the hotel to confirm "
            "available options and applicable charges."
        )
    },

    "laundry": {
        "question": "Does the hotel provide laundry or dry-cleaning services?",
        "answer": (
            "Laundry services may be available for guests who need clothing "
            "washed, pressed, or otherwise cared for. Charges and turnaround "
            "times depend on the service requested."
        )
    },

    "parking": {
        "question": "Does the hotel have parking facilities?",
        "answer": (
            "Parking availability depends on the hotel's facilities. Guests "
            "should confirm parking arrangements and availability with the hotel."
        )
    },

    "airport_transfer": {
        "question": "Does the hotel provide transportation or airport transfers?",
        "answer": (
            "Airport transfers or transportation services may be available "
            "upon request. Guests should contact the hotel in advance to "
            "confirm availability, pricing, pickup arrangements, and booking "
            "requirements."
        )
    },

    "business_facilities": {
        "question": "Does the hotel have facilities for business guests?",
        "answer": (
            "Business facilities may include meeting spaces, internet access, "
            "work areas, printing, or other services depending on the hotel's "
            "available facilities. Guests should contact the hotel to discuss "
            "their specific requirements."
        )
    },


    # --------------------------------------------------------
    # EVENTS, WEDDINGS & CELEBRATIONS
    # --------------------------------------------------------

    "wedding": {
        "question": "Can I host a wedding at the hotel?",
        "answer": (
            "Yes, wedding events may be hosted at JAHZ Empire Suites & Resort "
            "subject to venue availability and the hotel's event policies. "
            "The events team can discuss venue options, guest capacity, "
            "decoration, catering, seating arrangements, accommodation, "
            "entertainment, photography, and other wedding requirements."
        )
    },

    "wedding_reception": {
        "question": "Can I hold a wedding reception at the hotel?",
        "answer": (
            "Yes. Wedding receptions may be arranged subject to available "
            "event space and the preferred date. Couples can discuss guest "
            "capacity, venue setup, catering, decoration, music, entertainment, "
            "and other arrangements with the events team."
        )
    },

    "traditional_wedding": {
        "question": "Can I have my traditional wedding or engagement ceremony at the hotel?",
        "answer": (
            "Traditional weddings, introductions, engagement ceremonies, and "
            "other cultural celebrations may be accommodated subject to venue "
            "availability and hotel policies. The hotel can discuss the suitable "
            "space, setup, catering, decoration, and other requirements."
        )
    },

    "birthday": {
        "question": "Can I celebrate my birthday at the hotel?",
        "answer": (
            "Yes. Birthday celebrations may be arranged subject to venue "
            "availability. Guests can enquire about event space, food, drinks, "
            "decoration, music, seating, cake arrangements, and other services."
        )
    },

    "surprise_birthday": {
        "question": "Can I organize a surprise birthday party at the hotel?",
        "answer": (
            "A surprise birthday celebration may be possible. Guests should "
            "discuss their plans with the events team in advance so the hotel "
            "can advise on suitable spaces, timing, decoration, catering, "
            "and coordination."
        )
    },

    "anniversary": {
        "question": "Can I host an anniversary celebration at the hotel?",
        "answer": (
            "Yes. Anniversary dinners, parties, private celebrations, and "
            "other special occasions may be arranged depending on the hotel's "
            "available facilities and venue availability."
        )
    },

    "bridal_shower": {
        "question": "Can I organize a bridal shower or baby shower at the hotel?",
        "answer": (
            "Yes, where suitable event space is available. The hotel can "
            "discuss seating arrangements, catering, decorations, guest "
            "capacity, and other requirements."
        )
    },

    "graduation": {
        "question": "Can I organize a graduation party at the hotel?",
        "answer": (
            "Yes. Graduation celebrations may be arranged in an appropriate "
            "event space, subject to availability and the hotel's event policies."
        )
    },

    "naming_ceremony": {
        "question": "Can I hold a naming ceremony at the hotel?",
        "answer": (
            "Yes, subject to availability of a suitable event space. The hotel "
            "can discuss guest capacity, seating, catering, decoration, and "
            "other arrangements."
        )
    },

    "family_gathering": {
        "question": "Can I host a funeral reception or family gathering at the hotel?",
        "answer": (
            "Depending on the hotel's facilities and policies, suitable spaces "
            "may be available for family gatherings or receptions. Guests should "
            "contact the events team to discuss the nature and requirements of "
            "the gathering."
        )
    },

    "corporate_event": {
        "question": "Can I organize a corporate event at the hotel?",
        "answer": (
            "Yes. The hotel may accommodate corporate meetings, conferences, "
            "seminars, workshops, training sessions, presentations, staff "
            "events, and corporate dinners, subject to venue availability."
        )
    },

    "meeting_conference": {
        "question": "Can I organize a meeting or conference at the hotel?",
        "answer": (
            "Yes, subject to availability of an appropriate meeting or event "
            "space. The hotel can discuss seating arrangements, audiovisual "
            "requirements, refreshments, meals, and other conference needs."
        )
    },

    "product_launch": {
        "question": "Can I host a product launch at the hotel?",
        "answer": (
            "Product launches may be accommodated depending on the size and "
            "requirements of the event. The events team can discuss venue "
            "layout, branding, displays, guest capacity, catering, sound, "
            "lighting, and other requirements."
        )
    },

    "photoshoot": {
        "question": "Can I organize a photoshoot at the hotel?",
        "answer": (
            "Photography or video shoots may be permitted in designated areas "
            "subject to hotel policies and availability. Commercial or "
            "large-scale shoots may require prior approval and additional charges."
        )
    },

    "external_decorator": {
        "question": "Can I bring my own event decorator?",
        "answer": (
            "This depends on the hotel's event policy. External decorators "
            "may be permitted subject to prior approval and any conditions "
            "set by the hotel."
        )
    },

    "external_caterer": {
        "question": "Can I bring my own caterer for an event?",
        "answer": (
            "Outside catering may or may not be permitted depending on the "
            "hotel's event policy. Guests should confirm this with the events "
            "team before making arrangements with an external caterer."
        )
    },

    "event_decoration": {
        "question": "Does the hotel provide event decoration?",
        "answer": (
            "Decoration services may be available directly through the hotel "
            "or approved event partners. Guests can discuss their preferred "
            "theme, colours, stage design, table arrangement, flowers, lighting, "
            "and other decorative requirements with the events team."
        )
    },

    "event_catering": {
        "question": "Can the hotel provide food and drinks for my event?",
        "answer": (
            "Catering options may be available for weddings, birthdays, "
            "meetings, conferences, parties, and other events. Menus and "
            "pricing can be discussed with the events team based on the "
            "type and size of the event."
        )
    },

    "event_entertainment": {
        "question": "Can I arrange music, a DJ, or live entertainment for my event?",
        "answer": (
            "Entertainment may be permitted depending on the event space, "
            "operating hours, noise restrictions, and hotel policies. Guests "
            "should discuss entertainment plans with the events team in advance."
        )
    },

    "event_booking_time": {
        "question": "How far in advance should I book an event venue?",
        "answer": (
            "Guests are advised to reserve event venues as early as possible, "
            "especially for weddings, weekends, festive periods, and large "
            "celebrations. Early booking gives guests a better opportunity "
            "to secure their preferred date and arrangements."
        )
    },

    "event_packages": {
        "question": "Does the hotel offer event packages?",
        "answer": (
            "Event packages may be available depending on the type of event. "
            "Packages may combine venue hire, catering, decoration, accommodation, "
            "and other services. Guests should contact the events team for "
            "current packages and pricing."
        )
    },

    "wedding_guest_accommodation": {
        "question": "Can my wedding guests stay at the hotel?",
        "answer": (
            "Yes, subject to room availability. Group accommodation can be "
            "arranged for wedding guests, families, bridal parties, and other "
            "event attendees."
        )
    },

    "event_guest_rooms": {
        "question": "Can I reserve rooms for my event guests?",
        "answer": (
            "Yes. Group room reservations can be discussed with the hotel's "
            "reservations team. Depending on the size of the group, special "
            "arrangements may be available."
        )
    },

    "venue_inspection": {
        "question": "Can I inspect the event venue before booking?",
        "answer": (
            "A venue viewing may be arranged subject to availability. Guests "
            "are encouraged to discuss their event requirements with the hotel "
            "before the inspection so the most suitable space can be shown."
        )
    },

    "event_cost": {
        "question": "How much does it cost to host an event at the hotel?",
        "answer": (
            "Event pricing depends on the type of event, venue, number of "
            "guests, duration, catering, decoration, equipment, accommodation, "
            "and additional services. The hotel can prepare a quotation based "
            "on the guest's specific requirements."
        )
    },

    "event_enquiry_information": {
        "question": "What information should I provide when enquiring about an event?",
        "answer": (
            "For an accurate quotation, provide the type of event, preferred "
            "date, estimated number of guests, preferred venue or setup, "
            "catering requirements, decoration needs, entertainment plans, "
            "accommodation requirements, and any special requests."
        )
    },


    # --------------------------------------------------------
    # FAMILIES, GROUPS & SPECIAL OCCASIONS
    # --------------------------------------------------------

    "group_accommodation": {
        "question": "Does the hotel accommodate groups?",
        "answer": (
            "Yes. Group accommodation may be available for families, companies, "
            "wedding parties, tour groups, event attendees, and other organized "
            "groups. Larger groups should contact the hotel in advance."
        )
    },

    "family_stay": {
        "question": "Can families stay at the hotel?",
        "answer": (
            "Yes. Families can select rooms according to their number of "
            "occupants and accommodation requirements, subject to the hotel's "
            "occupancy policies."
        )
    },

    "romantic_stay": {
        "question": "Can I arrange a romantic stay or special surprise for my partner?",
        "answer": (
            "Special arrangements may be possible depending on the hotel's "
            "available services. Guests can discuss options such as room "
            "decoration, special meals, flowers, or other surprises with "
            "the hotel in advance."
        )
    },

    "special_room_arrangement": {
        "question": "Can the hotel help arrange a special occasion in my room?",
        "answer": (
            "Depending on hotel policy, special room arrangements may be "
            "possible. Guests should make their request before arrival so "
            "the hotel can confirm what can be provided."
        )
    },


    # --------------------------------------------------------
    # SAFETY, SECURITY & GUEST ASSISTANCE
    # --------------------------------------------------------

    "emergency": {
        "question": "What should I do if I have an emergency during my stay?",
        "answer": (
            "Guests should immediately contact the front desk or hotel "
            "management. Hotel staff will assist according to the hotel's "
            "emergency procedures and, where necessary, contact the appropriate "
            "emergency services."
        )
    },

    "lost_property_policy": {
        "question": "How does the hotel handle lost property?",
        "answer": (
            "Items found on hotel premises are handled according to the "
            "hotel's lost-and-found procedures. Guests should report missing "
            "belongings promptly so staff can assist with the search."
        )
    },

    "complaint": {
        "question": "Who should I contact if I have a complaint during my stay?",
        "answer": (
            "Guests should contact the front desk or hotel management as soon "
            "as possible. Reporting an issue promptly gives the hotel an "
            "opportunity to investigate and resolve it during the guest's stay."
        )
    },

    "special_requirements": {
        "question": "Can the hotel assist guests with special requirements?",
        "answer": (
            "Guests with specific accommodation, mobility, dietary, celebration, "
            "or other requirements should inform the hotel before arrival. "
            "The hotel can confirm which requests it can accommodate."
        )
    },


    # ========================================================
    # LOCATION, LANDMARKS & NEARBY ATTRACTIONS
    # ========================================================

    "airport_proximity": {
        "question": "Is JAHZ Empire Hotel & Suites close to the airport?",
        "answer": (
            "No. JAHZ Empire Hotel & Suites is not close to Murtala Muhammed "
            "International Airport. The hotel is located in Abijo along the "
            "Lekki-Epe Expressway. Travel time to the airport can vary "
            "significantly depending on traffic conditions."
        ),
    },

    "nearest_airport": {
        "question": "Which airport is closest to JAHZ Empire Hotel & Suites?",
        "answer": (
            "Murtala Muhammed International Airport is the main international "
            "airport serving Lagos. However, JAHZ Empire Hotel & Suites is "
            "not located close to the airport. Guests who need airport "
            "transport arrangements should contact the hotel directly."
        ),
    },

    "nearby_landmarks": {
        "question": "What landmark is JAHZ Empire Hotel & Suites close to?",
        "answer": (
            "JAHZ Empire Hotel & Suites is located around Kingdom Hall Bus Stop "
            "in Abijo, along the Lekki-Epe Expressway. Other recognizable places "
            "around the wider area include Novare Mall, LUFASI Nature Park, "
            "Giwa Gardens and several other attractions along the Lekki-Epe corridor."
        ),
    },

    "novare_mall": {
        "question": "Is JAHZ Empire Hotel & Suites close to Novare Mall?",
        "answer": (
            "Yes. Novare Mall is one of the recognizable shopping landmarks "
            "around the Lekki-Epe and Sangotedo area. Guests can contact the "
            "hotel for the best directions from the hotel to the mall."
        ),
    },

    "lufasi_nature_park": {
        "question": "Is JAHZ Empire Hotel & Suites close to LUFASI Nature Park?",
        "answer": (
            "Yes. LUFASI Nature Park is one of the nearby attractions in the "
            "area. It is a convenient recreational destination for guests who "
            "want to enjoy nature and outdoor activities."
        ),
    },

    "recreational_centres": {
        "question": "Is JAHZ Empire Hotel & Suites close to any recreational centre?",
        "answer": (
            "Yes. The hotel is located within the Lekki-Epe corridor, where "
            "guests can find several recreational and leisure attractions, "
            "including LUFASI Nature Park and other entertainment destinations."
        ),
    },

    "nearby_recreational_places": {
        "question": "What recreational places are near JAHZ Empire Hotel & Suites?",
        "answer": (
            "Some recreational and leisure attractions within the wider area "
            "include LUFASI Nature Park, Giwa Gardens, Lekki Conservation Centre, "
            "beaches and other leisure destinations along the Lekki-Epe corridor."
        ),
    },

    "nearby_beaches": {
        "question": "Is JAHZ Empire Hotel & Suites close to a beach?",
        "answer": (
            "Yes. There are several beaches and beach resorts within the wider "
            "Lekki area. Atican Beach is one of the recognizable beach destinations "
            "in the area. Travel time may vary depending on traffic."
        ),
    },

    "lekki_conservation_centre": {
        "question": "Is JAHZ Empire Hotel & Suites close to Lekki Conservation Centre?",
        "answer": (
            "JAHZ Empire Hotel & Suites is within the wider Lekki area and "
            "Lekki Conservation Centre can be reached from the hotel by road. "
            "Travel time depends on traffic conditions."
        ),
    },

    "giwa_gardens": {
        "question": "Is JAHZ Empire Hotel & Suites close to Giwa Gardens?",
        "answer": (
            "Yes. Giwa Gardens is one of the leisure and entertainment "
            "destinations within the wider Sangotedo and Lekki area. "
            "Guests can ask the hotel for directions when planning a visit."
        ),
    },

    "nearby_restaurants": {
        "question": "Are there restaurants near JAHZ Empire Hotel & Suites?",
        "answer": (
            "Yes. There are restaurants and food outlets along the Lekki-Epe "
            "corridor. JAHZ Empire Hotel & Suites also provides restaurant "
            "services for guests."
        ),
    },

    "easy_to_locate": {
        "question": "Is JAHZ Empire Hotel & Suites easy to locate?",
        "answer": (
            "Yes. The hotel is located at 14 Gbadamosi Alomaja Street, "
            "Kingdom Hall Bus Stop, Abijo, along the Lekki-Epe Expressway, Lagos. "
            "Kingdom Hall Bus Stop and the Lekki-Epe Expressway are useful "
            "landmarks when locating the hotel."
        ),
    },

    "nearest_major_road": {
        "question": "What major road is JAHZ Empire Hotel & Suites close to?",
        "answer": (
            "JAHZ Empire Hotel & Suites is located along the Lekki-Epe Expressway "
            "in the Abijo area of Lagos."
        ),
    },

    "nearby_shopping_centres": {
        "question": "Are there shopping centres near JAHZ Empire Hotel & Suites?",
        "answer": (
            "Yes. Novare Mall is one of the recognizable shopping destinations "
            "around the wider area. Guests can contact the hotel for directions "
            "to nearby shopping centres."
        ),
    },

    "nearby_tourist_attractions": {
        "question": "Are there tourist attractions near JAHZ Empire Hotel & Suites?",
        "answer": (
            "Yes. Guests can visit several attractions within the wider Lekki-Epe "
            "area, including LUFASI Nature Park, Giwa Gardens, Lekki Conservation "
            "Centre, beaches and other leisure destinations."
        ),
    },

    "good_location_for_lagos_attractions": {
        "question": "Is JAHZ Empire Hotel & Suites a good location for visiting attractions in Lagos?",
        "answer": (
            "Yes. The hotel's location along the Lekki-Epe corridor provides "
            "access to attractions and leisure destinations around Abijo, "
            "Sangotedo and the wider Lekki area."
        ),
    },


    # --------------------------------------------------------
    # GENERAL ENQUIRIES
    # --------------------------------------------------------

    "hotel_location": {
        "question": "Where is the hotel located?",
        "answer": (
            "JAHZ Empire Hotel & Suites is located at "
            "14 Gbadamosi Alomaja Street, Kingdom Hall Bus Stop, "
            "Abijo, Lekki-Epe Expressway, Lagos."
        )
    },

    "hotel_contact": {
        "question": "How can I contact the hotel?",
        "answer": (
            "Guests can contact JAHZ Empire Hotel & Suites through the "
            "official telephone numbers +234 706 275 4478 and "
            "+234 806 951 9327, or by email at "
            "info@jahzempiresuites.com."
        )
    },

    "speak_before_booking": {
        "question": "Can I speak with someone before making a booking?",
        "answer": (
            "Yes. Guests can contact the hotel before booking to ask questions "
            "about rooms, prices, events, facilities, special arrangements, "
            "or other hotel services."
        )
    },

    "request_quotation": {
        "question": "Can I request a quotation before booking?",
        "answer": (
            "Yes. Guests can request a quotation for accommodation, events, "
            "group bookings, conferences, weddings, celebrations, catering, "
            "or other hotel services. The quotation will depend on the "
            "guest's specific requirements."
        )
    },

    "hotel_promotions": {
        "question": "How can I find out about current hotel offers and promotions?",
        "answer": (
            "Current promotions may be announced through the hotel's official "
            "website and official communication channels. Guests should confirm "
            "that an offer is genuine and review its terms before making payment."
        )
    },

    "general_enquiry": {
        "question": "Can I make an enquiry without booking immediately?",
        "answer": (
            "Yes. Guests can contact JAHZ Empire Suites & Resort to ask "
            "questions, request availability, discuss an event, obtain a "
            "quotation, or learn more about available services before deciding "
            "whether to book."
        )
    },
}


# ============================================================
# HOTEL FAQ SEARCH TOOL
# ============================================================

def search_hotel_faq(query: str) -> list:
    """
    Search JAHZ Empire Suites & Resort frequently asked questions.

    The tool searches both FAQ questions and their answers and returns
    the most relevant matching FAQs.
    """

    if not query:
        return []

    query = str(query).lower().strip()

    if not query:
        return []

    # Normalize common variations
    normalized_query = (
        query
        .replace("-", " ")
        .replace("/", " ")
        .replace(",", " ")
        .replace(".", " ")
        .replace("?", " ")
    )

    query_words = set(normalized_query.split())

    results = []

    keywords = {

        "book": [
            "booking",
            "reservation",
            "reserve",
            "book",
        ],

        "booking": [
            "booking",
            "reservation",
            "reserve",
            "book",
        ],

        "reservation": [
            "reservation",
            "booking",
            "reserve",
            "book",
        ],

        "reserve": [
            "reservation",
            "booking",
            "reserve",
            "book",
        ],

        "room": [
            "room",
            "suite",
            "accommodation",
        ],

        "rooms": [
            "room",
            "suite",
            "accommodation",
        ],

        "suite": [
            "suite",
            "room",
            "accommodation",
        ],

        "pay": [
            "payment",
            "pay",
            "account",
            "cash",
        ],

        "paying": [
            "payment",
            "pay",
            "account",
            "cash",
        ],

        "payment": [
            "payment",
            "pay",
            "account",
            "cash",
        ],

        "cash": [
            "cash",
            "payment",
            "pay",
        ],

        "bank": [
            "account",
            "payment",
            "bank",
        ],

        "account": [
            "account",
            "payment",
            "bank",
        ],

        "wedding": [
            "wedding",
            "reception",
            "traditional",
        ],

        "birthday": [
            "birthday",
            "celebration",
            "party",
        ],

        "event": [
            "event",
            "venue",
            "celebration",
            "party",
        ],

        "party": [
            "party",
            "celebration",
            "event",
        ],

        "hotel": [
            "hotel",
            "resort",
        ],

        "resort": [
            "hotel",
            "resort",
        ],

        "cancel": [
            "cancel",
            "cancellation",
        ],

        "cancellation": [
            "cancel",
            "cancellation",
        ],

        "refund": [
            "refund",
            "cancellation",
        ],

        "checkin": [
            "check in",
            "check-in",
            "arrival",
        ],

        "check": [
            "check",
            "arrival",
            "departure",
        ],

        "checkout": [
            "check out",
            "check-out",
            "departure",
        ],

        "arrival": [
            "arrival",
            "early",
            "late",
            "check-in",
        ],

        "food": [
            "food",
            "catering",
            "restaurant",
            "dining",
        ],

        "restaurant": [
            "restaurant",
            "dining",
            "food",
        ],

        "catering": [
            "catering",
            "food",
            "event",
        ],

        "decor": [
            "decoration",
            "decorator",
        ],

        "decoration": [
            "decoration",
            "decorator",
        ],

        "decorator": [
            "decoration",
            "decorator",
        ],

        "dj": [
            "music",
            "dj",
            "entertainment",
        ],

        "music": [
            "music",
            "dj",
            "entertainment",
        ],

        "flight": [
            "flight",
            "flights",
            "air peace",
            "air ticket",
        ],

        "flights": [
            "flight",
            "flights",
            "air peace",
            "air ticket",
        ],

        "pool": [
            "pool",
            "swimming",
        ],

        "swimming": [
            "swimming",
            "pool",
        ],

        "gym": [
            "gym",
            "fitness",
            "exercise",
            "workout",
        ],

        "fitness": [
            "gym",
            "fitness",
            "exercise",
            "workout",
        ],

        "shortlet": [
            "shortlet",
            "short-let",
            "short let",
            "apartment",
        ],

        "apartment": [
            "apartment",
            "shortlet",
            "short-let",
        ],

        # ----------------------------------------------------
        # LOCATION SEARCH KEYWORDS
        # ----------------------------------------------------

        "airport": [
            "airport",
            "murtala",
            "airport transfer",
        ],

        "murtala": [
            "airport",
            "murtala",
            "airport transfer",
        ],

        "lagos": [
            "lagos",
            "attractions",
            "location",
        ],

        "location": [
            "location",
            "landmark",
            "address",
            "area",
            "road",
        ],

        "landmark": [
            "landmark",
            "location",
            "novare",
            "lufasi",
            "giwa",
        ],

        "landmarks": [
            "landmark",
            "location",
            "novare",
            "lufasi",
            "giwa",
        ],

        "novare": [
            "novare",
            "mall",
            "shopping",
        ],

        "mall": [
            "mall",
            "shopping",
            "novare",
        ],

        "shopping": [
            "shopping",
            "mall",
            "novare",
        ],

        "lufasi": [
            "lufasi",
            "nature",
            "park",
            "recreation",
        ],

        "nature": [
            "nature",
            "park",
            "lufasi",
        ],

        "park": [
            "park",
            "lufasi",
            "recreation",
        ],

        "recreation": [
            "recreation",
            "recreational",
            "leisure",
            "entertainment",
            "lufasi",
        ],

        "recreational": [
            "recreation",
            "recreational",
            "leisure",
            "entertainment",
        ],

        "leisure": [
            "leisure",
            "recreation",
            "entertainment",
            "attractions",
        ],

        "beach": [
            "beach",
            "beaches",
            "atican",
        ],

        "beaches": [
            "beach",
            "beaches",
            "atican",
        ],

        "atican": [
            "atican",
            "beach",
            "beaches",
        ],

        "giwa": [
            "giwa",
            "gardens",
            "entertainment",
        ],

        "gardens": [
            "gardens",
            "giwa",
            "attractions",
        ],

        "conservation": [
            "conservation",
            "lekki conservation",
            "nature",
            "attractions",
        ],

        "tourist": [
            "tourist",
            "attractions",
            "leisure",
            "recreation",
        ],

        "attraction": [
            "attraction",
            "attractions",
            "tourist",
            "leisure",
            "recreation",
        ],

        "attractions": [
            "attraction",
            "attractions",
            "tourist",
            "leisure",
            "recreation",
        ],

        "restaurants": [
            "restaurant",
            "restaurants",
            "dining",
            "food",
            "we are open 24 hours",
        ],

        "road": [
            "road",
            "expressway",
            "lekki-epe",
        ],

        "expressway": [
            "expressway",
            "road",
            "lekki-epe",
        ],

        "abijo": [
            "abijo",
            "location",
            "address",
            "kingdom hall",
        ],

        "kingdom": [
            "kingdom hall",
            "bus stop",
            "abijo",
        ],

        "bus": [
            "bus stop",
            "kingdom hall",
            "abijo",
        ],

        "nearby": [
            "nearby",
            "location",
            "landmark",
            "attractions",
            "recreation",
        ],

        "near": [
            "nearby",
            "location",
            "landmark",
            "attractions",
            "recreation",
        ],
    }

    for faq_id, faq in JAHZ_HOTEL_FAQ.items():

        question = faq["question"].lower()
        answer = faq["answer"].lower()

        searchable_text = f"{question} {answer}"

        normalized_searchable_text = (
            searchable_text
            .replace("-", " ")
            .replace("/", " ")
            .replace(",", " ")
            .replace(".", " ")
            .replace("?", " ")
        )

        searchable_words = set(
            normalized_searchable_text.split()
        )

        score = 0

        # Direct word matching
        for word in query_words:

            if word in searchable_words:
                score += 1

        # Related keyword matching
        for word in query_words:

            if word in keywords:

                for related_word in keywords[word]:

                    normalized_related_word = (
                        related_word
                        .lower()
                        .replace("-", " ")
                    )

                    if (
                        normalized_related_word
                        in normalized_searchable_text
                    ):
                        score += 2

        # Phrase matching
        phrases = [
            "room reservation",
            "room booking",
            "book a room",
            "hotel booking",
            "cash payment",
            "pay cash",
            "payment method",
            "payment methods",
            "payment account",
            "check in",
            "check out",
            "late check out",
            "early check in",
            "wedding reception",
            "traditional wedding",
            "birthday party",
            "surprise birthday",
            "bridal shower",
            "baby shower",
            "family gathering",
            "group accommodation",
            "airport transfer",
            "room service",
            "event decoration",
            "event catering",
            "hotel membership",
            "air peace",
            "short let",

            # Location phrases
            "close to the airport",
            "close to airport",
            "nearest airport",
            "near the airport",
            "near airport",
            "close to novare mall",
            "near novare mall",
            "close to lufasi",
            "near lufasi",
            "lufasi nature park",
            "recreational centre",
            "recreational center",
            "recreational centres",
            "recreational centers",
            "recreational places",
            "nearby attractions",
            "tourist attractions",
            "nearby tourist attractions",
            "close to a beach",
            "near a beach",
            "nearby beaches",
            "lekki conservation centre",
            "lekki conservation center",
            "giwa gardens",
            "near restaurants",
            "nearby restaurants",
            "shopping centres",
            "shopping centers",
            "nearby shopping",
            "easy to locate",
            "major road",
            "lekki epe expressway",
            "kingdom hall bus stop",
            "where is the hotel",
            "hotel location",
        ]

        for phrase in phrases:

            if (
                phrase in normalized_query
                and phrase in normalized_searchable_text
            ):
                score += 4

        if score > 0:

            results.append({
                "id": faq_id,
                "question": faq["question"],
                "answer": faq["answer"],
                "score": score,
            })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:5]

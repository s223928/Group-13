# DS/EN 16798-1 Method 1 tables (qp and qB)

QP_TABLE = {  # l/s per person
    "I": 10.0,
    "II": 7.0,
    "III": 4.0,
    "IV": 2.5,
}

QB_TABLE = {  # l/s per m2, by IEQ category and pollution class
    "I": {"LPB-1": 0.5,  "LPB-2": 1.0, "LPB-3": 2.0},
    "II": {"LPB-1": 0.35, "LPB-2": 0.7, "LPB-3": 1.4},
    "III": {"LPB-1": 0.2,  "LPB-2": 0.4, "LPB-3": 0.8},
    "IV": {"LPB-1": 0.15, "LPB-2": 0.3, "LPB-3": 0.6},
}


def choose_ieq_category() -> str:
    """
    Ask user for IEQ category (I, II, III, IV).
    """
    ieq = input("Select IEQ Category (I, II, III, IV): ").strip().upper()
    valid = {"I", "II", "III", "IV"}
    while ieq not in valid:
        print("Invalid category. Please select from I, II, III, IV.")
        ieq = input("Select IEQ Category (I, II, III, IV): ").strip().upper()
    return ieq


def choose_pollution_class() -> str:
    """
    Ask user for pollution class (LPB-1, LPB-2, LPB-3).
    """
    pollution = input(
        "Select Pollution Class "
        "(LPB-1 (very low polluting), LPB-2 (Low Polluting), LPB-3 (Non low-polluting)): "
    ).strip().upper()

    valid = {"LPB-1", "LPB-2", "LPB-3"}
    while pollution not in valid:
        print("Invalid class. Please select from LPB-1, LPB-2, LPB-3.")
        pollution = input(
            "Select Pollution Class "
            "(LPB-1 (very low polluting), LPB-2 (Low Polluting), LPB-3 (Non low-polluting)): "
        ).strip().upper()

    return pollution


def ventilation_rate_method_1(occupants: int, area: float,
                              ieq_category: str, pollution_class: str) -> float:
    """
    DS/EN 16798-1 Method 1:
    q_tot = n * qp + A * qB  [L/s]
    Also enforces minimum 4 L/s per person.
    """
    ieq = ieq_category.upper()
    lpb = pollution_class.upper()

    # Look up qp and qB
    qp = QP_TABLE[ieq]
    qB = QB_TABLE[ieq][lpb]

    # Base flow (people + building)
    q_tot = occupants * qp + area * qB

    # Minimum per person flow: 4 L/s per person
    q_min_people = occupants * 4.0
    q_final = max(q_tot, q_min_people)

    return q_final


# Simple interactive use (for testing)
if __name__ == "__main__":
    ieq = choose_ieq_category()
    lpb = choose_pollution_class()

    # Example: 5 people, 15.2 m2
    q = ventilation_rate_method_1(occupants=5, area=15.2,
                                  ieq_category=ieq, pollution_class=lpb)

    print(f"Calculated Ventilation Rate (Qtot): {q:.2f} L/s")

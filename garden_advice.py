import datetime

# TODO: Replace hardcoded month names with a programmatic solution (e.g., calendar module)
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def get_season(month):
    """Returns the season for a given month number."""
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"


def get_advice(month):
    season = get_season(month)

    if season == "Winter":
        tips = [
            "Protect plants from frost with mulch or covers.",
            "Plan your spring garden layout.",
            "Order seeds from catalogues.",
            "Clean and sharpen gardening tools."
        ]
    elif season == "Spring":
        tips = [
            "Start sowing seeds indoors.",
            "Prepare and enrich soil with compost.",
            "Begin planting cold-hardy vegetables.",
            "Watch out for late frosts."
        ]
    elif season == "Summer":
        tips = [
            "Water plants early morning or evening.",
            "Deadhead flowers to encourage blooming.",
            "Watch for pests and treat early.",
            "Harvest vegetables regularly."
        ]
    else:
        tips = [
            "Plant spring-flowering bulbs.",
            "Collect and compost fallen leaves.",
            "Divide and transplant perennials.",
            "Clear out spent summer plants."
        ]

    return season, tips


def display_advice(month_number, month_name):
    """Print seasonal gardening tips for the given month.

    Args:
        month_number: Integer 1-12 representing the month.
        month_name: String name of the month to display in the heading.
    """
    season, tips = get_advice(month_number)
    print(f"\n=== Gardening Advice for {month_name} ({season}) ===")
    for tip in tips:
        print(f"  - {tip}")


def get_user_month():
    """Prompt the user to enter a month name or press Enter for the current month.

    Returns a tuple of (month_number, month_name).
    Keeps asking until a valid month name is entered.
    """
    current_month = datetime.datetime.now().month
    current_month_name = MONTHS[current_month - 1]

    while True:
        user_input = input(f"Enter a month name (or press Enter for {current_month_name}): ").strip().title()
        if user_input == "":
            return current_month, current_month_name
        if user_input in MONTHS:
            return MONTHS.index(user_input) + 1, user_input
        print(f"'{user_input}' is not a valid month. Please try again.")


print("Welcome to the Garden Advice App!")
month_number, month_name = get_user_month()
display_advice(month_number, month_name)
print("\nTip: Consistent gardening throughout the year leads to a thriving garden!")

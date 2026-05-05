import datetime

# TODO: Replace hardcoded month names with a programmatic solution (e.g., calendar module)
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# TODO: Extract season logic into a separate function called get_season(month)
def get_advice(month):
    if month in [12, 1, 2]:
        season = "Winter"
        tips = [
            "Protect plants from frost with mulch or covers.",
            "Plan your spring garden layout.",
            "Order seeds from catalogues.",
            "Clean and sharpen gardening tools."
        ]
    elif month in [3, 4, 5]:
        season = "Spring"
        tips = [
            "Start sowing seeds indoors.",
            "Prepare and enrich soil with compost.",
            "Begin planting cold-hardy vegetables.",
            "Watch out for late frosts."
        ]
    elif month in [6, 7, 8]:
        season = "Summer"
        tips = [
            "Water plants early morning or evening.",
            "Deadhead flowers to encourage blooming.",
            "Watch for pests and treat early.",
            "Harvest vegetables regularly."
        ]
    else:
        season = "Autumn"
        tips = [
            "Plant spring-flowering bulbs.",
            "Collect and compost fallen leaves.",
            "Divide and transplant perennials.",
            "Clear out spent summer plants."
        ]
    return season, tips

# TODO: Add a docstring to this function explaining parameters and return value
def display_advice(month_number, month_name):
    season, tips = get_advice(month_number)
    print(f"\n=== Gardening Advice for {month_name} ({season}) ===")
    for tip in tips:
        print(f"  - {tip}")

# TODO: Create a function to get and validate user input instead of inline logic
current_month = datetime.datetime.now().month
current_month_name = MONTHS[current_month - 1]

print("Welcome to the Garden Advice App!")
print(f"Current month: {current_month_name}")

display_advice(current_month, current_month_name)

# TODO: Allow user to query advice for any month, not just the current one
print("\nTip: Consistent gardening throughout the year leads to a thriving garden!")

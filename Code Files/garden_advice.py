def get_season_advice(season):
    """
    Get gardening advice based on the season.
    
    Args:
        season (str): The current season (summer, winter, spring, autumn)
    
    Returns:
        str: Gardening advice for the specified season
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """
    Get gardening advice based on the plant type.
    
    Args:
        plant_type (str): The type of plant (flower, vegetable)
    
    Returns:
        str: Gardening advice for the specified plant type
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """
    Main function to run the gardening advice application.
    Gets user input and provides personalized gardening advice.
    """
    # Hardcoded values for the season and plant type
    season = "summer"  # TODO: Replace with input() to allow user interaction.
    plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

    # Generate gardening advice
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Print the generated advice
    print(advice)


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.

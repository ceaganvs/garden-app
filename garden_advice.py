month_tips = {
    "January": [
        "Plan your garden layout and order seeds for the coming season.",
        "Start seeds indoors for peppers and tomatoes.",
        "Check stored bulbs for rot and discard any that are soft.",
    ],
    "February": [
        "Sow sweet peas and broad beans under cover.",
        "Prune autumn-fruiting raspberries down to ground level.",
        "Begin hardening off seedlings started in January.",
    ],
    "March": [
        "Direct sow carrots, parsnips, and peas once soil warms.",
        "Apply a layer of compost around fruit trees.",
        "Watch for slugs as new growth emerges.",
    ],
    "April": [
        "Plant potatoes once frost risk has passed.",
        "Sow courgettes, squash, and beans indoors.",
        "Hoe beds regularly to keep weeds down.",
    ],
    "May": [
        "Transplant tomato seedlings to their final positions.",
        "Pinch out side-shoots on cordon tomatoes weekly.",
        "Water consistently — dry spells in May stress young plants.",
    ],
    "June": [
        "Harvest lettuce, radishes, and early peas.",
        "Feed tomatoes and peppers with a high-potash fertiliser.",
        "Deadhead flowers to encourage more blooms.",
    ],
    "July": [
        "Water deeply twice a week rather than a little every day.",
        "Summer-prune trained fruit trees (espaliers, fans).",
        "Begin harvesting courgettes before they turn to marrows.",
    ],
    "August": [
        "Sow spring cabbages and kale for an autumn crop.",
        "Dry and store onions once the tops fall over.",
        "Cut back spent herbs to encourage a flush of new growth.",
    ],
    "September": [
        "Plant spring bulbs — daffodils, tulips, and alliums.",
        "Harvest winter squash before the first frost.",
        "Take cuttings from tender perennials before temperatures drop.",
    ],
    "October": [
        "Mulch beds heavily to protect roots from frost.",
        "Lift and divide overcrowded perennials.",
        "Clear fallen leaves off lawns to prevent die-back.",
    ],
    "November": [
        "Plant bare-root trees, roses, and hedging while soil is workable.",
        "Dig over empty beds and add well-rotted manure.",
        "Insulate outdoor containers with fleece or bubble wrap.",
    ],
    "December": [
        "Clean and oil garden tools before storing for winter.",
        "Check stored fruits and vegetables for signs of rot.",
        "Plan next year's crop rotation to reduce soil-borne disease.",
    ],
}

SEASONS = {
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"],
    "Autumn": ["September", "October", "November"],
    "Winter": ["December", "January", "February"],
}


def get_tips_for_month(month):
    tips = month_tips.get(month)
    if tips is None:
        return f"No tips found for '{month}'."
    lines = [f"Tips for {month}:"]
    for i, tip in enumerate(tips, 1):
        lines.append(f"  {i}. {tip}")
    return "\n".join(lines)


def get_tips_for_season(season):
    months = SEASONS.get(season)
    if months is None:
        return f"No season called '{season}'. Try Spring, Summer, Autumn, or Winter."
    lines = [f"{season} tips:"]
    for month in months:
        lines.append(f"\n{month}:")
        for tip in month_tips[month]:
            lines.append(f"  - {tip}")
    return "\n".join(lines)


def main():
    print("Garden Advice Tool")
    print("==================")
    # TODO: add a search feature so users can look up tips by keyword (e.g. 'tomato', 'frost')
    print("\nEnter a month name, a season, or 'quit' to exit.")
    while True:
        user_input = input("\n> ").strip().title()
        if user_input in ("Quit", "Q", "Exit"):
            print("Happy gardening!")
            break
        elif user_input in month_tips:
            print(get_tips_for_month(user_input))
        elif user_input in SEASONS:
            print(get_tips_for_season(user_input))
        else:
            # TODO: suggest the closest matching month/season when the user types something unrecognised
            print("Type a month (e.g. 'April') or season (e.g. 'Summer').")


if __name__ == "__main__":
    main()

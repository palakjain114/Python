def sort_food_items():
    food_items = [("Burger", 120), ("Pizza", 250), ("Pasta", 180), ("Sandwich", 100)]
    sorted_food = sorted(food_items, key=lambda item: item[1], reverse=True)

    print("Food items sorted by price (Descending):")
    for item in sorted_food:
        print(item)

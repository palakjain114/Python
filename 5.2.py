def find_occurrences():
    numbers = [random.randint(1, 10) for _ in range(20)]
    print(f"Generated List: {numbers}")

    user_input = int(input("Enter a number to find its occurrences: "))
    positions = [i for i, num in enumerate(numbers) if num == user_input]

    if positions:
        print(f"{user_input} found at positions: {positions}")
    else:
        print(f"{user_input} not found in the list.")

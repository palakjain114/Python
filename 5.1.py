def process_odd_even_lists():
    odd_list = [random.choice(range(1, 100, 2)) for _ in range(5)]
    even_list = [random.choice(range(2, 100, 2)) for _ in range(4)]

    print(f"Original odd list: {odd_list}")
    print(f"Original even list: {even_list}")

    odd_list[2] = even_list  # Replace 3rd element with even list
    print(f"Modified odd list: {odd_list}")

    flat_list = sorted([num for sublist in odd_list for num in (sublist if isinstance(sublist, list) else [sublist])])
    print(f"Flattened and sorted list: {flat_list}")

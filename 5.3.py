def remove_duplicates():
    numbers = [random.randint(1, 30) for _ in range(50)]
    unique_numbers = list(set(numbers))
    print(f"Original List: {numbers}")
    print(f"List after removing duplicates: {unique_numbers}")

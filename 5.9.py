def difference_of_lists():
    list1 = [random.randint(1, 20) for _ in range(10)]
    list2 = [random.randint(1, 20) for _ in range(5)]

    result_list = [num for num in list1 if num not in list2]

    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Numbers in List 1 but not in List 2: {result_list}")

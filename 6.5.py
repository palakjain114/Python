def remove_empty_tuples():
    tuple_list = [("Apple", 50), (), ("Banana", 30), (), ("Grapes", 60)]
    cleaned_list = [t for t in tuple_list if t]

    print(f"List after removing empty tuples: {cleaned_list}")

def modify_tuple():
    my_tuple = (10, 20, 30)
    temp_list = list(my_tuple)
    temp_list[1] = 99 
    my_tuple = tuple(temp_list)

    print(f"Modified tuple: {my_tuple}")

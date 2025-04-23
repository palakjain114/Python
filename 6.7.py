def delete_tuple_element():
    my_tuple = (10, 20, 30)
    temp_list = list(my_tuple)
    temp_list.remove(20)  
    my_tuple = tuple(temp_list)

    print(f"Tuple after deletion: {my_tuple}")

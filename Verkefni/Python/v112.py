def is_int(str_to_test):
    try:
        int(str_to_test)
        return True
    except:
        return False



def list_to_int_tuple(search_list):
    int_list = []
    int_tub = ()
    for item in search_list:
        if is_int(item):
            int_list.append(int(item))

    int_tub = tuple(int_list)
    return int_tub
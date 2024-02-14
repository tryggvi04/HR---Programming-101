


def list_to_bool_tuple(a_list):
    bool_list = []

    for item in a_list:
        item = item.strip()
        if item.isdecimal():
            bool_list.append(bool(int(item)))
        else:
            bool_list.append(bool(item))

    return tuple(bool_list)
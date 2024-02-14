def without_outliers(a_list):
    copy_list = a_list[:]
    new_list = a_list[:]
    copy_list.sort()
    new_list.remove(copy_list[0])
    new_list.remove(copy_list[-1])
    return new_list

def remove_min_and_max(a_list):
    copy_list = a_list[:]
    copy_list.sort()
    a_list.remove(copy_list[0])
    a_list.remove(copy_list[-1])
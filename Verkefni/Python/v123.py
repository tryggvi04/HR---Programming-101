def extract_evens(int_list):
    new_list = int_list
    res = []

    for num in new_list:
        if int(num) % 2 == 0:
            res.append((num))
    return res

def remove_odds(int_list):
    copy_list = int_list[:]
    for i in range(0, len(copy_list)):
        if int(copy_list[i]) % 2 != 0:
            int_list.remove(copy_list[i])




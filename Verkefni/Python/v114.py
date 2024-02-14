def list_to_float(a_list):
    ret_list = []
    for item in a_list:
        ret_list.append(float(item))
    return ret_list

def score_sum(seq):
    seq_list = seq.split()
    sum_num = 0
    length = len(seq_list)
    seq_list = list_to_float(seq_list)
    seq_list = sorted(seq_list)

    if length > 2:
        for item in seq_list[3:]:
            sum_num += item
        return f"Sum of scores (3 lowest removed): {round(sum_num, 1)}"
    
    else:
        return "At least 3 scores needed!"

print(score_sum(input()))
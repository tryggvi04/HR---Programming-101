def sum_of_range(start: int, end: int, step: int):
    res = 0
    for i in range(int(start), int(end)+1, int(step)):
        res += i
    return res


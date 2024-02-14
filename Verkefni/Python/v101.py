def find_squares(n):
    import math
    count_list = []
    for i in range(1, n+1):
        count_list.append(i**2)
    return count_list
        
print(find_squares(int(input())))
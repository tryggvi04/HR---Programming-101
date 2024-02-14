
def is_file(string_to_try):
    ''' Boolean function where we try to open the input and test if its a valid file'''
    try: 
        file = open(string_to_try)
        return True
    except:
        return False


def is_float(string_to_try):
    ''' Boolean function to test if a string is a float or not'''
    try:
        float(string_to_try)
        return True
    except:
        return False

def cumulative_sum(seq: list):
    ''' Takes in a list and returns the cumulative sum of that list, in a list'''
    sum = 0
    length = len(seq)
    sum_list = []
    for i in range(0, length):
        sum += seq[i]
        num = round(sum, 4)
        sum_list.append(str(num))
    return sum_list


def median_in_list(seq: list):
    ''' Takes in a list and returns the median of the list'''

    length = len(seq) 
    median = length / 2
    
    
    if length%2 == 0:
        median = int(median)
        ceiling = seq[median]
        floor = seq[median-1]
        median_even = (ceiling+floor)/2
        return round(median_even, 4)
    else:
        pos = (length-1)/2
        pos = int(pos)
        num = seq[pos]
        return round(num, 4)



def sequence_analysis(file_name: str):
    data_file = open(file_name)
    seq = []

    #collect all the digits or floats in a list called seq
    for line in data_file:

        line = line.strip('\n')

        if is_float(line):
            seq.append(float(line))

    if seq != []:
        #step 1
        for item in seq:
            print(round(item, 4), end=(" "))
        print("")
        


        #step 2
        print(" ".join(cumulative_sum(seq)))


        #step 3
        seq_sorted = sorted(seq)
        for item in seq_sorted:
            print(round(item, 4), end=(" "))
        print("")
        

        #step 4
        print(median_in_list(seq_sorted))






file_name = str(input())

if is_file(file_name):
    sequence_analysis(file_name)
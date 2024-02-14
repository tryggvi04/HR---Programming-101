def collect_digits(str_list: list):
    ''' Takes in a list and returns all the digits in a list '''

    digit_list = []

    for char in str_list:
        if char.isdigit():
            digit_list.append(int(char))
    return digit_list


def missing_numbers(digit_list: list):
    ''' Takes in a list of digits and finds the missing gaps '''

    sorted_list = sorted(digit_list)
    filled_list = []
    max_int = max(sorted_list)

    for i in range(0, max_int+1):

        if i not in sorted_list:
            filled_list.append(i)

    return filled_list



# Part 1
input_list = input().split()

print(input_list)

# Part 2

digit_list = collect_digits(input_list)

print(digit_list)

# Part 3

if digit_list != []:

    filled_list = missing_numbers(digit_list)

    print(filled_list)
else:
    print(digit_list)
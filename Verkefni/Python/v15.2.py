import string

def file_to_set(file_name: str):
    data_file = open(file_name)
    data_set = set()

    for line in data_file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation)
            data_set.add(word)
    return data_set

def string_format(sentence: list):
    new_sentence = ""
    if len(sentence) != 1:
        for i in range(0, len(sentence)):
            if sentence[i] == sentence[len(sentence)-1]:
                new_sentence += sentence[i] + "."
            elif sentence[i] == sentence[len(sentence)-2]:
                new_sentence += sentence[i] + " and "
            else:
                new_sentence += sentence[i] + ", "
    else:
        new_sentence += sentence[0]
    return new_sentence 


def f_Intersection(set1: set, set2: set):
    intersection_set = set1.intersection(set2)
    intersection_list = list(intersection_set)
    intersection_list = sorted(intersection_list)

    formatted_string = string_format(intersection_list)

    print(f"The two files have {len(intersection_set)} words in common.")
    print("These words are as follows:")
    print(formatted_string)
    print("")

def s_difference(set1: set, set2: set):
    difference_set = set1.symmetric_difference(set2)
    difference_list = list(difference_set)
    difference_list = sorted(difference_list)

    formatted_string = string_format(difference_list)

    print(f"There are {len(difference_set)} words that are only in either file but not both.")
    print("These words are as follows:")
    print(formatted_string)
    print("")

def f_difference(set1: set, set2: set):
    difference_set = set1.difference(set2)
    difference_list = list(difference_set)
    difference_list = sorted(difference_list)

    formatted_string = string_format(difference_list)

    print(f"There are {len(difference_set)} words that only appear in the first file.")
    print("These words are as follows:")
    print(formatted_string)
    print("")


set1 = file_to_set(input())
set2 = file_to_set(input())


print("")
f_Intersection(set1, set2)
s_difference(set1, set2)
f_difference(set1, set2)


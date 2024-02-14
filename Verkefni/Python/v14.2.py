import string

def sort_dict(a_dict: dict):
    ''' Takes in a dictinary and sorts the keys in alphabetical order '''

    sorted_list = sorted(a_dict)
    sorted_dict = {}

    for key in sorted_list:
        sorted_dict[key] = a_dict[key]
        
    return sorted_dict

def collecting_dictinaries(sentence: str):
    letter_dict = {}
    for char in sentence:
        char = char.lower()
        if char not in string.punctuation and char != " ":
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    
    return letter_dict

sentence_one = str(input())
sentence_two = str(input())

dict1 = collecting_dictinaries(sentence_one)
dict2 = collecting_dictinaries(sentence_two)

sorted_dict1 = sort_dict(dict1)
sorted_dict2 = sort_dict(dict2)


if dict1 == dict2:
    print(f"{sentence_one} is an anagram of {sentence_two}.")

else:
    print(f"{sentence_one} is not an anagram of {sentence_two}.")
    

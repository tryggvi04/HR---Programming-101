def is_file(file_name: str):
    ''' Boolean function that takes in a file name and checks if it's a real file that can be opened '''

    try: 
        open(file_name)
        return True
    except:
        return False

def collecting_words(file_name: str):
    ''' Takes in a file name and returns all the words in a list '''

    word_file = open(file_name)
    word_list = []
    for line in word_file:

        # Create a list of words in a given line
        line = line.strip()
        line = line.split()

        for word in line:
            word_list.append(word)
            
    return word_list

def removing_punctuation(word_list: list):
    ''' Takes in a list of words and separetes the punctuation around them '''
    word_str = ""
    puncuation_str = ""
    letter_list = []

# Check each individual character and check whether is a letter or a puncuation, then we add them to our letter list accordingly
    for word in word_list:
        for char in word:
            if char.isalpha():
                word_str += char
            else:
                puncuation_str += char               

        letter_list.append(word_str)

        if puncuation_str != "":
            letter_list.append(puncuation_str)
        word_str = ""
        puncuation_str = ""
            

    return letter_list


file_name = input()

if is_file(file_name):

    word_list = collecting_words(file_name)


    # Part 1

    print(len(word_list))
    print('\n'.join(word_list))


    # Part 2

    letter_list = removing_punctuation(word_list)
    print(len(letter_list))
    print('\n'.join(letter_list))
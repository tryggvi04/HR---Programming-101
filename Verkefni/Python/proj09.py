import string

FILE_NAME = input()
continue_bool = True

def is_file(file_name: str):
    ''' Tests a string to see whether it's a file that can be opened, boolean function '''

    try:
        file_to_try = open(file_name)
        return True

    except:
        return False
    
def Document_to_list(file_name: str):
    ''' Takes a file of documents and returns a list of strings of the documents '''

    data_file = open(file_name)
    document_list = []
    current_doc = ""

    for line in data_file:
        line = line.strip('\n')
        if line != "<END OF DOCUMENT>":
            line = line.split()

            for word in line:
                word = word.strip()
                current_doc += word + " "
        else:
            document_list.append(current_doc.strip())
            current_doc = ""
    return document_list

def list_to_dict(document_list: list):
    ''' Takes a list of documents and returns a dictionary with each word as a key and the document it was in as the value '''

    document_dict = {}

    for i, document in enumerate(document_list):
        document = document.split(" ")
        for word in document:
            word = word.lower()
            word = word.strip(string.punctuation)
            # We check whether word is already in the dict or not, if it is we just add it to the existing set, if it isn't we create a set.
            if word in document_dict:
                    document_dict[word].add(i + 1)
            else:
                document_dict[word] = {i + 1}

    return document_dict

def main(doc_dict: dict, doc_list: list):

    user_input = input().lower()

    if user_input == "search":
        search(doc_dict)
        return True

    elif user_input == "print":
        print_doc(doc_list)
        return True

    else:
        return False
        



def search(doc_dict: dict):
    ''' Allows the user to input a string and then it prints which document(s) the sentence appears in '''

    input_str = input().lower()
    search_list = input_str.split()
    match_set = set()

# Create our inital set, it will try to find the first search word, returning an empty set if nothing is found
    match_set = set(doc_dict.get(search_list[0], set()))

    for word in search_list:
        # Intersection will always give set() if we couldn't find anything in our initial set so we loop through every search word and find
        # the intersection between our found documents list and the new word, always giving an empty set if the get function couldn't find anything.
        match_set = match_set.intersection(doc_dict.get((word), set()))
            
    match_list = sorted(list(match_set))
    if match_set == set():
        print("No match")
    else:
        print("Documents matching search:", *match_list)


            
def print_doc(docu_list: list):
    ''' Takes in an integer input from the user and prints the document matching the index '''

    doc_index = int(input())

    if len(docu_list) >= doc_index and doc_index > 0:
        print(f"Document #{doc_index}:")
        print(docu_list[doc_index - 1])
    else:
        print("No match")
        


if is_file(FILE_NAME):
    document_list = Document_to_list(FILE_NAME)

    document_dict = list_to_dict(document_list)

    while continue_bool == True:
        # We turn the main function into a boolean function, returning true if the user asks for print or search but giving false at anything else.
        continue_bool = main(document_dict, document_list)


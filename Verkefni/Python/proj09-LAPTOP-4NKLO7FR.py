import string

file_name = input()

def Document_to_list(file_name: str):
    ''' Takes a file of documents and returns a list of said documents '''

    data_file = open(file_name)
    document_list = []
    current_doc = ""

    for line in data_file:
        line = line.strip('\n')
        if line != "<END OF DOCUMENT>":
            line = line.split()

            for word in line:
                word = word.strip(string.punctuation)
                current_doc += word.lower() + " "
        else:
            document_list.append(current_doc.strip())
            current_doc = ""
    return document_list

def list_to_dict(document_list: list):
    ''' Takes a list of documents and returns a dictionary with each word as a key and the document it was in as the value '''

    document_dict = {}

    for i, document in enumerate(document_list):
        document = document.split()
        for word in document:
            if word in document_dict:
                document_dict[word] += str(i) + " "
            else:
                document_dict[word] = str(i) + " "

    return document_dict

def main(doc_dict: dict):
    ''' A controller function that checks what the user wants to do and finds the right function to use '''

    user_input = input()
    if user_input == "search":
        search(doc_dict)



def search(doc_dict: dict):
    ''' Allows the user to input a string and then it prints which document(s) the word appears in '''

    search_str = input().lower()
    match_list = []
    for key, value in doc_dict.items():
        if key == search_str:
            if value not in match_list:
                match_list.append(value)
    if match_list == []:
        print("No match")
    else:
        print("Documents matching search:", " ".join(match_list))
            



document_list = Document_to_list(file_name)

document_dict = list_to_dict(document_list)

main(document_dict)

def is_file(file_name: str):
    ''' Tests a string to see whether it's a file that can be opened, boolean function '''
    try:
        file_to_try = open(file_name)
        return True

    except:
        return False

def get_file():
    valid_name = False

    while valid_name == False:
        file_to_test = input()

        if is_file(file_to_test):
            valid_name = True
        else:
            print("File", file_to_test, "not found!")
        
    return file_to_test
def get_contries(file_name):
    list_countries = []
    countries_file = open(file_name)

    for line in countries_file:
        line = line.strip()
        list_countries.append(line)
    return list_countries

def len_dict(countries_list: list):
    length_dict = {}

    for country in countries_list:
        length = len(country)
        if length in length_dict:
            length_dict[length].append(country)
        else:
            length_dict[length] = [country]
    return length_dict

def find_len_country(length_dict: dict):
    continue_str = "y"

    while continue_str == "y":
        len_index = int(input())
        
        if len_index in length_dict:
            print(", ".join(length_dict[len_index]))
        else:
            print(f"No country name of length {len_index} exists.")
        continue_str = input().lower()

file_name = get_file()

countries_list = get_contries(file_name)

length_dict = len_dict(countries_list)

find_len_country(length_dict)


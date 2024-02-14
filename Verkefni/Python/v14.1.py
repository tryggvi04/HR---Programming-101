continue_str = "y"
siggi_dict = {}

while continue_str == "y":

    key_input = input()
    value_input = input()
    continue_str = input()

    siggi_dict[key_input] = value_input

def sort_dict(a_dict: dict):
    ''' Takes in a dictinary and sorts the keys in alphabetical order '''

    sorted_list = sorted(a_dict)
    sorted_dict = {}

    for key in sorted_list:
        sorted_dict[key] = a_dict[key]
        
    return sorted_dict


sorted_dict = sort_dict(siggi_dict)

for key in sorted_dict:
    print("")
    print(f"{key}:")
    print(f"    {sorted_dict[key]}")


def extract_first_number_from_string(string_to_search):
    res = ""
    num_bool = False
    if any(char.isdecimal() for char in string_to_search):
        for char in string_to_search:
            if char.isdecimal() == True:
                num_bool = True
                res += char
            if char.isdecimal() == False and num_bool == True:
                break
            
            
        return int(res)

    return -1        
    
print(extract_first_number_from_string(input("Input: ")))
def collect_digits(a_str):
    '''Here we cycle through the string and collect the decimals in a string'''
    result_str = ""
    if any(char.isdecimal() for char in a_str):
        for char in a_str:
            if char.isdecimal() == True:
                result_str += char
            
            
            
    return result_str
    

def inverse_case(a_str):
    '''Here we cycle through the string and check if its uppercase, and if it is, then we reverse it in another string and vice versa '''
    result_str = ""
    for char in a_str:
        if char == char.upper():
            result_str += char.lower()
        else:
            result_str += char.upper()
    return result_str
    

def to_hex(an_int):
    '''We divide with 16 and collect the remainders in an array then create the hex number with the appropriate numbers/letters'''

    res_str = ""
    current_int = an_int
    hex_array = []
    while current_int > 0:
        remainder = current_int % 16
        hex_array.append(str(remainder))
        current_int = current_int // 16
    if an_int == 0:
        return "0"
    hex_array.reverse()
    for num in hex_array:
        hex_letters = ["A", "B", "C", "D", "E", "F"]
        if int(num) > 9:
            placement = int(num)-10
            res_str += hex_letters[placement]
        else:
            res_str += str(num)
    return(res_str)

def string_functions(option_char):
    if option_char == "c":
        print(collect_digits(input()))
    elif option_char == "i":
        print(inverse_case(input()))
    elif option_char == "h":
        print(to_hex(int(input())))
    elif option_char == "q":
        quit()

while True:
    string_functions(input())

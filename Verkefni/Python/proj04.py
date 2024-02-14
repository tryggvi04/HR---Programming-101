passw_str = ""
invalid_int = 0
valid_int = 0
count_int = 0
invalid_bool = False



while passw_str != "q":
    passw_str = str(input())
    if passw_str == "q":
        break
    count_int += 1
    length_int = len(passw_str)

    if length_int < 6 or length_int > 20:
        invalid_int += 1
        print(f"{passw_str}: Invalid length.")
        continue

    if any(char.islower() for char in passw_str) == False:
        invalid_bool = True
        print(f"{passw_str}: Missing lower case letter.")

    if any(char.isupper() for char in passw_str) == False:
        invalid_bool = True
        print(f"{passw_str}: Missing upper case letter.")

    if any(char.isnumeric() for char in passw_str) == False:
        invalid_bool = True
        print(f"{passw_str}: Missing numeric letter.")
        
    if invalid_bool == False:
        valid_int += 1
        print(f"{passw_str}: Valid password of length {length_int}.")
    else:
        invalid_int += 1
        invalid_bool = False
    

print(f"You tried {count_int} passwords, {valid_int} valid, {invalid_int} invalid.")

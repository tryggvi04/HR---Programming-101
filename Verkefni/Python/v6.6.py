a_str = input()

name_str = a_str.split(",")

first_name = name_str[0].strip()
last_name = name_str[1].strip()

last_name = last_name.upper()
first_name = first_name.capitalize()



print(f"{last_name[0]}. {first_name}")
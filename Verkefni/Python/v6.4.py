a_str = input()
res = ""

for char in a_str:
    if char == char.upper():
        res += char.lower()
    else:
        res += char.upper()
print(res)
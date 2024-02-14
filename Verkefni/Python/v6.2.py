a_str = input()  # Do not change this line
res = ""

for i, char in enumerate(a_str):
    if i%2 == 0 or i == 0:
        res += char
print(res)
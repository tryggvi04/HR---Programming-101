a_str = str(input())
length = len(a_str)
res = ""

for i in range(length-1, 0-1, -1):
    res += a_str[i]

if a_str.lower() == res.lower():
    print("Palindrome!")
else:
    print("Nothing special about this string :(")
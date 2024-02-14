a_str = input()
char_to_count = input()

end = len(a_str)

for i in range(0, end):
    if a_str[i] == char_to_count:
        print(a_str.index(a_str[i], i))
def reverse(file_name):
    file_to_search = open(file_name)

    res = ""

    for line in file_to_search:
        line = line.split()
        for word in line:
            rev_word = word[::-1]
            res += rev_word
            res += " "
    return res
print(reverse(input()))
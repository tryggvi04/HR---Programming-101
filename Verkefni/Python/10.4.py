word_str = str(input())
word_list = [word_str.lower()]
l1 = [word_str]
l0 = []
while True:
    word_str = str(input()).lower()
    if word_str == "x":
        break
    if (word_str[0]) == (word_list[-1])[-1]:
        l1.append(word_str)
        word_list.append(word_str)
    else:
        l0.append(word_str)
print(" ".join(l1))
print(" ".join(l0))
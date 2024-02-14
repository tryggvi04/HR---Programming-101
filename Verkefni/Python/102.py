n = int(input())
original_list = []
for i in range(0, n):
    original_list.append(input())
    

reverse_list = reversed(original_list)

for item in reverse_list:
    print(item)
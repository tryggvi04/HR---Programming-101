address_input = ""
address_list = []
address_split = []
address_tub = ()

while address_input != 'q':
    address_input = str(input())
    if address_input == 'q':
        break

    address_list.append(address_input)


for item in address_list:
    address_split.append(tuple(item.split()))

print(address_list)
print(address_split)
num1 = int(input()) # Do not change this line
num2 = int(input()) # Do not change this line
num3 = int(input()) # Do not change this line

numbers = []
max_int = num1


numbers.append(num1)

numbers.append(num2)

numbers.append(num3)

for num in numbers:
    if (max_int - num <= 0):
        max_int = num

print(max_int) 
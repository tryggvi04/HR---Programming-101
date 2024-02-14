stop_range = int(input())
num_divisors = int(input())

count_int = 0


for i in range(10, stop_range):
    first_int = i//10
    second_int = i%10
    if pow((first_int + second_int), 2) == i:
        print(i)

for i in range(0, stop_range):
    count_int = 0
    for y in range(1, i + 1):
        if i % y == 0:
            count_int += 1
    if count_int == num_divisors:
        print(i)


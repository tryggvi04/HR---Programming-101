k = int(input())
n = int(input())
the_sum = 0

for i in range(1, n+1):
    x = int(input())
    the_sum += pow(k, x)

print(the_sum)
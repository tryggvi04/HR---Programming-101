mb_per_month = int(input())
n = int(input())
mb_allotted = 0

for i in range(1, n+1):
    wasted = int(input())
    mb_allotted += (mb_per_month-wasted)

mb_allotted += mb_per_month


print(mb_allotted)

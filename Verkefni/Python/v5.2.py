n = int(input())  # Do not change this line
seq = [1]
num = 1
for i in range (0, n):
    if i == 0:
        num += num
    elif i == 1:
        num += seq[i] + seq[i-1]
    else:
        num += seq[i] + seq[i-1] + seq[i-2]
    print(seq[i])
    seq.append(num)
    num = 0


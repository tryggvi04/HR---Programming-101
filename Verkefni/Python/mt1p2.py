num_int = 1
n = int(input())
series_float = 0.0


for i in range(0, n):
    num_int *= 1/2
    series_float += num_int
    print(series_float)
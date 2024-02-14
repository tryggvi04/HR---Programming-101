def are_permutation_of_same_digits(m: str, n: str):
    res = []
    met = []
    for char, char2 in zip(m, n):
        res.append(char)
        met.append(char2)
    res.sort()
    met.sort()
    if res == met:
        print(f"The numbers {m} and {n} are permutations of each other.")
    else:
        print(f"The numbers {m} and {n} are not permutations of each other.")
    


m = input()
n = input()
if are_permutation_of_same_digits(m, n) == True:
    print(f"The numbers {m} and {n} are permutations of each other.")

else:
    print(f"The numbers {m} and {n} are not permutations of each other.")
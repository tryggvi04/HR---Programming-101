def decide(number):
    sum_div = sum_of_divisors(number)
    if sum_div > number:
        return f"{number} is abundant."
    elif number > sum_div:
        return f"{number} is deficient."
    else:
        return f"{number} is a perfect number."
    

def sum_of_divisors(number: int):
    res_int = 0
    for i in range (1, number):
        if number % i  == 0:
            res_int += i
    return(res_int)
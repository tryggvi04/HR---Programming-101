answer = input("You need something doubled? (Y)es? ")

while answer == "Y":
    
    number = float(input("All right, then. Give me a number, and I'll double it for ya: "))
    number = number*2
    print(number)
    answer = input("You need something else doubled? (Y)es? ")
cost_int = int(input())
amount_payed = int(input())
change_int = amount_payed - cost_int
payed = False

while payed == False:
    if (change_int - 20) >= 0:
        change_int -= 20
        print("20")
        continue
    elif (change_int - 10) >= 0:
        change_int -= 10
        print("10")
        continue
    elif (change_int - 5) >= 0:
        change_int -= 5
        print("5")
        continue
    elif (change_int - 2) >= 0:
        change_int -= 2
        print("2")
        continue
    elif (change_int - 1) >= 0:
        change_int -= 1
        print("1")
        continue
    payed = True
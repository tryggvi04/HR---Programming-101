value_int = int(input())

if value_int == 9:
    print("Queen")
elif value_int == 5:
    print("Rook")
elif value_int == 3:
    print("Bishop or Knight")
elif value_int == 1:
    print("Pawn")
else:
    print("No piece")
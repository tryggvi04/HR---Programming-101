seven_found = False
number = int(input()) # Do not change this line

while number != 0:
    if int(number) % 10 == 7:
        seven_found = True
    number = number / 10

if seven_found: # Hint: does this variable name suggest anything?
    print("The number contains 7.")
else:
    print("The number does not contain 7.")


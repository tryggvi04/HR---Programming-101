year = int(input()) # Do not change this line

#step 1
if year % 4 == 0:

    # step 2
    if year % 100 == 0:

        #step 3
        if year % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")
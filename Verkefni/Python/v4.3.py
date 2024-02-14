size = int(input())

if size != 1:
    print("*", " *" * (size-1), end='', sep='')

    for i in range(1, size-1):
     print('\n', "*", " " * ((size-2)*2), " *", end='', sep='')

    print('\n', "*", " *" * (size-1), '\n', end='', sep='')
else:
    print("*", '\n', end='', sep='')
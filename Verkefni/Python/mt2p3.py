row = 1
column = 2

def creating_data(int_list):
    ''' Takes in a list and returns the matrixes of A and B '''
    
    max_int = row*column
    A = []
    B = []

    for i in range(0, max_int):
        A.append(int_list[i])

    for i in range(max_int, len(int_list)):
        B.append(int_list[i])

    return A, B

def matrix_sum(A: list, B: list):
    C = []
    sum_num = 0
    for a_num, b_num in zip(A, B):
        sum_num = a_num + b_num
        C.append(sum_num)
    return C

def creating_matrixes(A: list, B: list, C: list):
    ''' Takes in the lists of A, B and C and formats them into matrixes '''
    current_item = []

    A_matrix = []
    B_matrix = []
    C_matrix = []

    max_int = column*row


    # Formatting A
    for i in range(0, column):
        current_item.append(A[i])      
    A_matrix.append(current_item)
    current_item = []

    for i in range(column, max_int):
        current_item.append(A[i])
        
    A_matrix.append(current_item)
    current_item = []


    # Formatting B
    for i in range(0, column):
        current_item.append(B[i])      
    B_matrix.append(current_item)
    current_item = []
    
    for i in range(column, max_int):
        current_item.append(B[i])
        
    B_matrix.append(current_item)
    current_item = []

    # Formatting C
    for i in range(0, column):
        current_item.append(C[i])      
    C_matrix.append(current_item)
    current_item = []
    
    for i in range(column, max_int):
        current_item.append(C[i])
        
    C_matrix.append(current_item)
    current_item = []

    return A_matrix, B_matrix, C_matrix



list_int = []



for i in range(0, (row*column)*2):
    list_int.append(int(input()))

A, B = creating_data(list_int)

C = matrix_sum(A, B)

A_matrix, B_matrix, C_matrix = creating_matrixes(A, B, C)

print(A_matrix)
print(B_matrix)
print(C_matrix)



    
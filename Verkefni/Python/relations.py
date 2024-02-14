# T-117-STR1 Discrete Mathematics I
# Template for Individual assignment 5
# Problem 1a)
def is_reflexive(defined_set, relation_on_set: list):
    # We go through each number in the defined set and if there's a tuple of the same number we return true.
    for item in defined_set:
        mirrored = (item, item)
        if mirrored in relation_on_set:
            return True
    return False
        
# Problem 1b)
def is_symmetric(relation_on_set):
    # We go through each item in the relations set, if the tuple reversed exists in the set we return true.
    for item in relation_on_set:
        if (item[1], item[0]) not in relation_on_set:
            return False
            
    return True
# Problem 1c)
def is_antisymmetric(relation_on_set):
    # Same solution as in problem 1b only reversed.
    for item in relation_on_set:
        if (item[1], item[0]) in relation_on_set:
            return False
    return True
# Problem 1d)
def is_transitive(relation_on_set):
    # We create four variables, a, b, c and d. Then we loop through each tuple, with each variable being an item in the tuple then
    # we check whether there's any relation to a and d.
    for a, b in relation_on_set:
        for c, d in relation_on_set:
            if b == c:
                if (a, d) not in relation_on_set:
                    return False
    return True
# Problem 2
def is_equivalence_relation(defined_set, relation_on_set):
    # We go through each of the equivalence functions and check whether they're true or false, only returning true if all of them are true.
    reflexive = is_reflexive(defined_set, relation_on_set)
    symmetric = is_symmetric(relation_on_set)
    transitive = is_transitive(relation_on_set)

    if reflexive and symmetric and transitive:
        return True
    return False
# Problem 3
def composite_relations(relation1, relation2):
    # We use our knowledge of composite relations to create our list, we check every item in both lists and append the tuple when it's applicable.
    answer = []
    for item_1 in relation1:
        for item_2 in relation2:
            if item_1[1] == item_2[0] and (item_1[0], item_2[1]) not in answer:
                answer.append((item_1[0], item_2[1]))

    return answer
# Problem 4a)
def aces_in_relation_a(A):
    # We count every time an item in A is equal to 0.
    ace_count = 0

    for int in A:
        if int == 0:
            ace_count += 1
    return ace_count
# Problem 4b)
def aces_in_relation_b(A):
    # We go through every number and count the times the number + 1 is equal to the number above it.
    ace_count = 0

    for i in range(0, len(A)-1):
        B = A[i]+1
        if B == A[i+1]:
            ace_count += 1

    return ace_count
# Problem 4c)
def aces_in_relation_c(A):
    # For every number a we check every other number to see if a is bigger or equal to said number.
    ace_count = 0

    for a in A:
        for num in A:
            if a >= num:
                ace_count += 1

    return ace_count
# Problem 4d)
def aces_in_relation_d(A):
    ace_count = 0

    for a in A:
        for num in A:
            if a + num == 1000:
                ace_count += 1
    return ace_count
# Problem 5e)
def aces_in_relation_e(A):

    ace_count = 0

    for a in A:
        for num in A:
            if a + num >= 1001:
                ace_count += 1
    return ace_count
    



def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """
    first_lower = first.lower()
    second_lower = second.lower()

    if first_lower == second_lower:
        return first
    
    length_int = 0

    if len(first) > len(second):
        length_int = len(first)
    else:
        length_int = len(second)
    
    for i in range(0, length_int):
        if i > len(first)-1:
            return first
        elif i > len(second)-1:
            return second
        if first_lower[i] < second_lower[i]:
            return first
        elif second_lower[i] < first_lower[i]:
            return second
        else:
            continue

def is_substring_of(potential_substring: str, potential_superstring: str):
    if potential_superstring.find(potential_substring) != -1:
        return True
    else:
        return False
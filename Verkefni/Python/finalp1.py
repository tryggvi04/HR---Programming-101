from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.
MIN_DICE_RESULT = 1


def main():
    dice_result = get_input()
    # Makes the pogram keep running until an invalid input comes. 
    while validating_input(dice_result):
        dice_count = get_counts(dice_result)
        point_value = calculate_points(dice_count)
        print(point_value)
        dice_result = get_input()


def get_counts(dice_results: List[int]) -> List[int]:
    """Counts how often each value appears.

    Returns a list of counts
    for each possible outcome on a die roll,
    where the first count in the list
    (at position 0 in the output list)
    indicates how many 1's appear
    in the given list of dice results,
    the second count (at position 1)
    indicates how many 2's appear, and so on.
    The count list is as long as there are sides on the dice.

    For example, if the dice list is [3, 3, 4, 4, 1],
    then the count list is [1, 0, 2, 2, 0, 0],
    indicating that the number 1 appears once,
    the numbers 3 and 4 appear twice each,
    but the numbers 2, 5 and 6 never appear.
    """

    counts = [dice_results.count(value) for value in range(1, MAX_DICE_RESULT + 1)]
    return counts

def calculate_points(dice_count: List[int]) -> int:
    '''Find what combination the dice throw gave out, we'll be checking for three combinations.
    1. Yatzee, if the same numbered appeared five times.
    2. Three of a kind, if the same number appeared (at least) three times.
    3. Pair, find the highest value pair among the dice rolls.
    4. We don't have to worry about if every roll was unique because then the program returns the point value which was 0 by default.'''

    point_value: int = 0

    # We go through how many times each dice roll came up, then update our point value based on the rules above.
    # Because we keep updating our point value when a new combination comes along, the highest combination value will be the one thats kept.
    # We return the point value at Yatzee and Three of a kind since there's no higher combination that could be reached.
    for i, count in enumerate(dice_count):
        i += 1

        # Yatzee
        if count == 5:
            point_value = 50
            return point_value

        # Three of a kind
        elif count >= 3:
            point_value = i * 3
            return point_value

        # Pair
        elif count == 2:
            point_value = i * 2

    return point_value
        
def get_input() -> list[int]:
    '''Gets the input rolls from the user, returning a list of the rolls and validating whether the number fits within a dice roll'''
    input_result = input().split()
    dice_result = []
    
    for dice_roll in input_result:
        dice_roll = int(dice_roll)
        if dice_roll >= MIN_DICE_RESULT or dice_roll <= MAX_DICE_RESULT:
            dice_result.append(dice_roll)

    return dice_result

def validating_input(dice_result: list[int]) -> bool:
    '''Check whether the input was valid or not, boolean function.'''

    if len(dice_result) == 5:
        return True
    else:
        return False




if __name__ == "__main__":
    main()

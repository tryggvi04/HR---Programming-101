def main():
    input_list = get_data()
    
    print("Sorted list:", sorted(input_list))
    print("Composite list:", Composite_list(input_list))
    min_max(input_list)
    exit()


def get_data() -> list:
    """Asks user repeatedly for input until valid."""
    valid = False

    while valid == False:

        input_list = input().split(",")
        input_list = (check_data(input_list))
        if input_list != False:
            valid = True
            print("Input list:", input_list)
            return input_list
        else:
            print("Incorrect input! Please try again.")


    



def check_data(input_list: list):
    """Returns True or False on wether the list provided is valid."""
    correct_list = []
    for item in input_list:
        if not str(item).isdigit() or int(item) < 0:
            return False
        correct_list.append(int(item))
    return correct_list          
            
def Composite_list(input_list):

    comp_list = []

    for num in input_list:
        if is_prime(num) == False:
            if num not in comp_list:
                comp_list.append(num)
    
    return sorted(comp_list)

def min_max(input_list):

    min_num = min(input_list)
    max_num = max(input_list)
    average = sum(input_list)/len(input_list)

    print('Min: {}, Max: {}, Average: {:.2f}'.format(min_num, max_num, average))
   


# Add as many functions as you think you could use.


def is_prime(n: int) -> bool:
    """Returns True if the given positive number is prime and False otherwise."""

    if n < 2:
        return False

    for i in range(2, n):  # Feel free to improve this function if you like.
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()

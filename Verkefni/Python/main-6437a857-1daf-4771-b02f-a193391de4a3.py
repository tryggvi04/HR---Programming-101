from typing import Tuple

from v123 import remove_odds, extract_evens


def main():
    # You can use this for local testing:
    run_examples()
    # or
    run_samples()

    # Or run this to take input from terminal:
    run_like_gradescope()


def run_examples():
    # Example usage
    a_list = [1, 1, 2, 3, 4, 5]
    print(f"a_list initially: {a_list}")
    remove_odds(a_list)
    print(f"a_list after removing odds: {a_list}")

    b_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"b_list initially: {b_list}")
    c_list = extract_evens(b_list)
    print(f"b_list after extracting evens: {b_list}")
    print(f"c_list after extracting evens: {c_list}")


def run_samples():
    run_sample_1()
    run_sample_2()
    # Add the other samples yourself if you wish.


def run_sample_1():
    test_input = "1 1 2 3 4 5"
    int_list = get_int_list(test_input)
    output(int_list)


def run_sample_2():
    test_input = "10 7 7 7 7 1 10 9 9"
    int_list = get_int_list(test_input)
    output(int_list)


def get_int_list(test_input: str):
    return [int(string) for string in test_input.split()]


def output(int_list):
    print(f"Original list before calling functions: {int_list}")
    result = extract_evens(int_list)
    print(f"Resulting list after extracting evens: {result}")
    print(f"Original list after extracting evens and before removing odds: {int_list}")
    remove_odds(int_list)
    print(f"Original list after removing odds: {int_list}")


def run_like_gradescope():
    int_list = get_int_list(input())
    output(int_list)


if __name__ == "__main__":
    main()

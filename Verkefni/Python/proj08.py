MAX_GUESSES = 10

def is_file(file_name: str):
    ''' Tests a string to see whether it's a file that can be opened, boolean function '''

    try:
        file_to_try = open(file_name)
        return True

    except:
        return False

def selecting_word(file_name):
    ''' Asks the user for input and returns the secret word '''

    secret_index = int(input())
    word_list = []
    data_file = open(file_name)

    for line in data_file:

        line = line.strip()
        word_list.append(line)
        length_list = len(word_list)
        
        if length_list == secret_index:
            break
    secret_word = word_list[-1]
    return secret_word

def guessing_words(secret_word):
    ''' Allows the player to select a letter to guess from and prints if it's correct '''

    guessed_letters = []
    guess_count = 0
    found_bool = False
    guess_str = ""
    length_word = len(secret_word)
    correct_answers = 0

    for i in range(0, length_word):
        guessed_letters.append("-")


# The main loop that allows players to guess, and prints out the result of the game.
    while guess_count < MAX_GUESSES and correct_answers != length_word:
        found_bool = False
        print("Secret word:", *guessed_letters)
        print(f"Guess {guess_count}/{MAX_GUESSES}")
        guess_str = input()
        
        # If the character is already in the guessed list, we print correct letter but don't do anything else
        if guess_str not in guessed_letters:

            for i, char in enumerate(secret_word):

                if char == guess_str:

                    guessed_letters.insert(i, guess_str)
                    guessed_letters.pop(i+1)
                    correct_answers += 1
                    found_bool = True
        else:
            found_bool = True
            guess_count += 1

        if found_bool == True:
            print(f"Correct letter {guess_str}!")  

        else:
            print(f"Incorrect letter {guess_str}!")
            guess_count += 1



        # Win / Lose conditions
        if correct_answers == length_word: 
            print("Secret word:", *guessed_letters)
            print("You won!")
            break
        if guess_count == MAX_GUESSES:
            print("Secret word:", *guessed_letters)
            print("You lost! The secret word was", secret_word)
            break


file_name = str(input())

if is_file(file_name):
    secret_word = (selecting_word(file_name))
    guessing_words(secret_word)
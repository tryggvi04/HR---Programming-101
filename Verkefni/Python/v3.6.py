number_of_players = 0
# check for the number of players, asking again if the input isn't valid
while number_of_players < 2:
    number_of_players = int(input())
i = 0
num = 0
result = 0
#finding the summation of the contributions
while i < number_of_players:
    num = int(input())
    result += num
    i += 1

#calculating and printing the winner
winner = result%number_of_players
print("The sum of all contributions is", result)
print(f"When {result} is divided by {number_of_players}, the remainder is {winner}")
print("Player", winner, "is the winner!")



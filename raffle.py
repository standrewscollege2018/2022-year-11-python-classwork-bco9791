''' This program runs a raffle '''


# Start by importing the random package so we can randomly select a winner
import random

# Welcome
print("Welcome to the raffle program")

# Get prize, making sure that it isn't an empty input
fff = True
while fff == True:
    prize = input("What is the prize being raffled? ")
    if prize:
        fff = False
    else:
        print("Please enter a valid prize")

# Get value of prize, checking to make sure it is an integer
aaa = True
while aaa == True:
    try:
        value = int(input(f"What is the value of the {prize}? (do not input the $ sign) "))
        aaa = False
    except ValueError:
        print("Please input a valid integer")

# Declare list and entrants number        
names = []
entrants = 0

# Get names of entrants, checking for a blank input
enter_name = True
while enter_name == True:
    name = input("Enter name of entrant: ")
    if name == "end":
        enter_name = False
    else:
        if name:
            names.append(name)
            entrants += 1
        else:
            print("Please enter a valid name")

# Print the number of entrants 
print(f"There are {entrants} people in the draw for the {prize}")

# Check if there were no entrants and determine a winner
if entrants == 0:
    print("There were no winners")
else:
    number = random.randint(1,entrants)
    winner = names[number-1]
    print(f"And the winner of the {prize}, valued at ${value}, is... {winner}!")

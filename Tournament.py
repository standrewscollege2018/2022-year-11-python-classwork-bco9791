''' This program calculates tournament results '''


# Introduction and getting home team name
print("Welcome to the Super Tournament Points Calculation system")
g = True
while g == True:
    team1 = input("Enter the name of the team")
    if team1:
        g = False
    else:
        print("Please input a valid team name")
# Declare oppoenent list and receive all opponent team names
opponent_list = []
keep_asking = True
print("** Opponents **")
while keep_asking == True:
    opponent = input("Enter the name of an opponent (if done enter 'done')")
    if opponent.lower() == "done":
        keep_asking = False
    elif opponent:
        # Checking the input isn't empty
        opponent_list.append(opponent)
    else:
        print("Please enter a valid opposing team")
# Results
print("** Results **")
team1_score = 0
length = len(opponent_list)
# Print all results, increeasing the home team's total points based on the outcome of the game
for i in range(0,length):
    print(f"Game versus {opponent_list[i]}")
    score1_test = True
    negative = True
    while negative == True:
        while score1_test == True:
            score1_test = False
            try:
                score1 = int(input(f"{team1} score:"))
            
            except ValueError:
                # Making sure that the input is a number
                print("Enter a valid integer")
                score1_test = True
        if score1 < 0:
            print("Enter a valid integer")
        else:
            negative = False   
            
    score2_test = True
    negative2 = True
    while negative2 == True:
        while score2_test == True:
            score2_test = False
            try:
                score1 = int(input(f"{team1} score:"))
            
            except ValueError:
                # Making sure that the input is a number
                print("Enter a valid integer")
                score2_test = True
        if score2 < 0:
            print("Enter a valid integer")
        else:
            negative2 = False  
            
    if score1 == score2:
        print("You drew")
        team1_score += 2
    elif score1 > score2:
        print("You won!")
        team1_score += 3
    elif score1 < score2:
        print("You lost...")
        team1_score += 1
    else:
        print("Error")
# Print final stats
if length == 0:
    print("No opposing teams... so no points :)")
else:
    print("Competition complete!")
    print(f"{team1} finished the competition with {team1_score} points.")

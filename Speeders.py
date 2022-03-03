'''Fine calculation system'''

print("Welcome to the Speeers Fine Calculation system")
keep_asking = True
speed_limit_check = True
while keep_asking == True:
    name_check = True
    off_speed_check = True
    fine_check = True
    while name_check == True:
        name = input("Enter the name of the offender")
        if name.lower == "john smith" or name.lower == "helga norman" or name.lower == "zach conroy":
            print(f"** ALERT! There is an arrest warrant for {name} **")
        elif name.lower == "end":
            keep_asking = False
            off_speed_check = False
            fine_check = False
        elif name:
            name_check = False
        else:
            print("Please enter a valid name")
    while speed_limit_check == True:
        try:
            speed_limit = float(input("Enter the speed limit"))
        except ValueError:
            print("Please enter a valid integer")
        if speed_limit < 0:
            print("Please enter a valid speed limit")
        elif speed_limit == 0:
            print("How is anyone supposed to go anywhere?")
        else:
            speed_limit_check = False
    while off_speed_check == True:
        try:
            off_speed = float(input("Enter the offender's speed"))
        except ValueError:
            print("Please enter a valid speed")
        if off_speed < 0:
            print("Please enter a valid speed")
        elif off_speed == 0:
            print("Why")
            print("are")
            print("you")
            print("entering")
            print("someone")
            print("who")
            print("isn't")
            print("moving???")
        else:
            off_speed_check = False
    while fine_check == True:
        fine_check = False
        difference = off_speed - speed_limit
        if off_speed <= speed_limit:
            print("'Offender' has not broken the speed limit, let them go")
        elif difference < 10:
            print(f"{name} should be fined $30")
        elif difference < 20:
            print(f"{name} should be fined $80")
        

'''Program for renting out rental cars'''

print("Welcome to the University vehicle rental system")
vehicles = [["Suzuki Van", 2], ["Toyota Corolla", 4], ["Honda CRV", 4], ["Suzuki Swift", 4], ["Mitsubishi Airtrek", 4], ["Nissan DC Ute", 4], ["Toyota Previa", 7], ["Toyota Hi Ace", 12], ["Toyota Hi Ace", 12]]
names = []
unavailable = ["- available", "- available", "- available", "- available", "- available", "- available", "- available", "- available", "- available", "- available", "- available", "- available"]
booking_list = []
get_vehicles = True
while get_vehicles == True:
    print("The vehicles are:")
    for i in range(0, 9):
        print(f"{i+1}. {vehicles[i][0]} ({vehicles[i][1]})")
    get_vehicle = True
    get_input = True
    get_name = True
    get_confirmation = True
    # Bring all booleans up here
    while get_vehicle == True:
        while get_input == True:
            try:
                book = int(input("Which vehicle would you like to book? (type 0 to end the process)"))
                if book > 9 or book < 0:
                    print("Please enter a valid integer from 0-9")
                elif book == 0:
                    get_vehicle = False
                    get_input = False
                    get_vehicles = False
                    get_name = False
                    # Come back here to disable all loops
                elif book:
                    get_input = False
                    booking_list.append(book}
                else:
                    print("Please enter a valid integer from 0-9")
            except ValueError:
                print("Please enter a valid integer from 0-9")
        print("You have selected the {vehicle[book-1][0]")
        while get_confirmation == True:
            select = input("Is this selection correct?")
            if select.lower == "yes":
                get_vehicle = False
                get_confirmation = False
                unavailable[book-1] = "- unavailable"
            elif select.lower == "no":
                get_confirmation = False
                print("Please select another vehicle")
            else:
                print("Please enter yes or no")
    while get_name == True:
        name = input("Please enter your name")
        if name:
            if name.isalpha():
                get_name = False
                print(f"Thank you {name}")
                names.append(name)
        else:
            print("Please enter a valid name")
print("Daily Summary")
for i in range (1, len(names))
print(f"{vehicles[booking_list[i-1][0]} - {names[i-1]")

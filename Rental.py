'''Program for renting out rental cars'''

print("Welcome to the University vehicle rental system")
vehicles = [["Suzuki Van", 2], ["Toyota Corolla", 4], ["Honda CRV", 4], ["Suzuki Swift", 4], ["Mitsubishi Airtrek", 4], ["Nissan DC Ute", 4], ["Toyota Previa", 7], ["Toyota Hi Ace", 12], ["Toyota Hi Ace", 12]]
get_vehicles = True
while get_vehicles == True:
    print("The vehicles are:")
    for i in range(0, 9):
        print(f"{i+1}. {vehicles[i][0]} ({vehicles[i][1]})")
    get_vehicle = True
    get_input = True
    while get_vehicle == True:
        while get_input == True:
            try:
                book = int(input("Which vehicle would you like to book? (type 0 to end the process)"))
            except ValueError:
                print("Please enter a valid integer from 0-9")
            if book > 9 or book < 0:
                print("Please enter a valid integer from 0-9")
            elif book == 0:
                get_vehicle = False
                get_vehicles = False
                # Come back here to disable all remaining loops
            elif book:
                get vehicle = True
            else:
                print("Please enter a valid integer from 0-9")
    print("You have selected the {vehicle[book-1][0]")
    select = input("Is this selection correct?")
    if select == "Yes":
            get_vehicle = False
    else:
        print("Please select another vehicle")
        

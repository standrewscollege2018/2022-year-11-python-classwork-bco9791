'''Program for renting out rental cars'''

print("Welcome to the University vehicle rental system")
vehicles = [["Suzuki Van", 2], ["Toyota Corolla", 4], ["Honda CRV", 4], ["Suzuki Swift", 4], ["Mitsubishi Airtrek", 4], ["Nissan DC Ute", 4], ["Toyota Previa", 7], ["Toyota Hi Ace", 12], ["Toyota Hi Ace", 12]]
names = []
booking_list = []
unavailable = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
get_vehicles = True
while get_vehicles == True:
    print("The vehicles are:")
    for i in range(0, 9):
        print(f"{i+1}. {vehicles[i][0]} ({vehicles[i][1]}) {unavailable[i-1]}")
    get_input = True
    get_name = True
    while get_input == True:
         try:
             book = int(input("Which vehicle would you like to book? (type 0 to end the process)"))
             if book > 9 or book < 0:
                 print("Please enter a valid integer from 0-9")
             elif book == 0:
                 get_input = False
                 get_vehicles = False
                 get_name = False
                 # Come back here to disable all loops
             elif unavailable[book - 2] == "- unavailable":
                 print("** That car is already booked. Please choose another. **")
             elif book:
                 get_input = False
                 unavailable[book - 2] = "- unavailable"
                 booking_list.append(vehicles[book - 1][0])
             else:
                print("Please enter a valid integer from 0-9")
         except ValueError:  
             print("Please enter a valid integer from 0-9")
    print(f"You have selected the {vehicles[book - 1][0]}")    
    while get_name == True:
        name = input("Please enter your name")
        if name:
            if name.isalpha():
                if name not in names:
                    get_name = False
                    print(f"Thank you {name}")
                    names.append(name)
                else:
                    print("One car per person please")
            else:
                print("Please enter a valid name")
        else:
            print("Please enter a valid name")
print("Daily Summary")
for i in range (1, len(names)):
    print(f"booking_list[i-1]} - {names[i-1]}")

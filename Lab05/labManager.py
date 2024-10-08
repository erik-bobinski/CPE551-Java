# Author: Erik Bobinski
# Date: 10/4/2024
# Description: Add, remove, and display the equipment in a lab, max capacity of 5 items

equipment = [] # Lab inventory of equipment, max of 5 items

userIn = None # user input for switch statement
listIn = None # user input for equipment list
while(userIn != 4):
    userIn = int( input("1. Add Equipement\n2. Remove Equipment\n3. Display Current Equipment\n4. Leave the Laboratory Manger\n\n") )
    match userIn:
        case 1:
            if len(equipment) < 5:
                listIn = input("What piece of equipment would you like to add?\t")
                equipment.append(listIn)
                print(f"Added {listIn} to the laboratory\n")
            else:
                print("Cannot add more equipment, max of 5 items reached.")
        case 2:
            listIn = input("What piece of equipment would you like to remove?\t")
            if listIn in equipment:
                equipment.remove(listIn)
                print(f"{listIn} removed from the laboratory.\n")
            else:
                print(f"{listIn} not found in the laboratory.\n")
        case 3:
            if not equipment:
                print("The laboratory is empty\n")
            else:
                for item in equipment:
                    print(f"{item}", end=" ")
                print("\n")

        case 4:
            print("Exiting Laboratory Manager...\n")
            exit()
        case _:
            print("Input an integer [1-4] inclusively.\n") 

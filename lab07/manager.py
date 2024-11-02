# Author: Erik Bobinski
# Date: 11/2/2024
# Description: Allows user to interact with a warehouse
# Add and remove goods, and view the total amount of goods

from Warehouse import Warehouse

def main():
    warehouse = Warehouse(0)

    print("Welcome to the Warehouse!\n")

    choice = ""
    while choice != "4":
        choice = input("(1) Add Goods\n(2)Remove Goods\n"
        "(3)Output Total\n(4)Quit\n"
        "Which would you like?(input integer): ")

        match choice:
            case "1":
                try:
                    userInput = int(input("How many goods would you like to add?(integer only): " ))  
                    warehouse.addGoods(userInput)
                except ValueError:
                    print("Enter integers only")
            case "2":
                try:
                    userInput = int(input("How many goods would you like to remove?(integer only): " ))  
                    warehouse.removeGoods(userInput)
                except ValueError:
                    print("Enter integers only")
            case "3":
                print(f"Total Goods: {warehouse.getTotalGoods()}")
            case "4":
                print("Exiting Warehouse...")
            case _:
                print("Enter an integer between 1 and 4")

if __name__ == "__main__":
    main()

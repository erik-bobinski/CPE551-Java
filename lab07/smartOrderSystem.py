# Author: Erik Bobinski
# Date: 11/2/2024
# Description: Improved product ordering system that allows user-
# to shop for a several products via a list of objects

from smartProduct import SmartProduct

# calc total cost for product list
def calcTotal(prodList):
    total = 0
    for i in range(len(prodList)):
        total += prodList[i].getTotalCost()
    return total

def main():
    # list of product objects
    prodList = []

    # handle user-input for amount of products ordered
    while True:
        try:
            indexInput = int(input("How many products would you like to order (int): "))
            break
        except ValueError:
            print("Must enter an integer")

    # initialze user-specified amount of product objects
    for i in range(indexInput):
        name = input("Enter name of product: ")

        while True:
            try:
                qty = int(input(f"Quantity of {name} you would like to buy(int): "))
                break
            except ValueError:
                print("Must enter an integer")
                
        prodList.append(SmartProduct(name, qty, 9.99, i)) 

    print("")

    # output list of product info
    for i in range(len(prodList)):
        print(f"Product: {prodList[i].getName()}\n"
            f"Quantity: {prodList[i].getQty()}\n"
            f"Unit-Price: ${prodList[i].getUnitPrice():.2f}\n"
            f"Cost: ${prodList[i].getTotalCost():.2f}\n")
    print(f"Total Cost of Order: ${calcTotal(prodList):.2f}")

if __name__ == "__main__":
    main()

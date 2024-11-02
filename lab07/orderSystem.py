# Author: Erik Bobinski
# Date: 11/2/2024
# Description: Allows user to shop for a product and view its attributes

from Product import Product

def calcTotal(prodObj):
    return prodObj.getQty() * prodObj.getUnitPrice()

def main():
    prod = Product()

    name = input("What product would you like: ")
    prod.setName(name)

    # set product quantity, with error handling
    while True:
        try:
            qty = int(input(f"Quantity of {name} to purchase: "))
            prod.setQty(qty)
            break
        except ValueError:
            print("Invalid Input. Must enter an integer")

    unitPrice = 9.99
    prod.setUnitPrice(unitPrice)

    totalCost = calcTotal(prod)
    prod.setTotalCost(totalCost)

    # output of full order
    print(f"\nOrder Results:\nProduct: {name}\nQuantity: {qty}\nUnit Price: ${unitPrice}\nTotal Cost: ${totalCost:.2f}")

if __name__ == "__main__":
    main()

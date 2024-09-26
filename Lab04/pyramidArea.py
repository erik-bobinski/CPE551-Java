# Author: Erik Bobinski
# Date: 9/24/2024
# Description: Calculates the surface area of the base, sides,
#  and total surface area of a square pyramid

# function definitions
def calcBaseArea(side):
    return side ** 2

# add your function definition for calcSideArea here
def calcSideArea(side, height):
    return (2*side) * ( ( (side**2) /4) + (height ** 2) ) ** (1/2)  

# add your function definition for prntSurfArea here
def prntSurfArea(side, height):
    print(calcBaseArea(side) + calcSideArea(side, height))

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))

    height = float(input("Enter the height of the square pyramid in feet: "))

    base_area = calcBaseArea(side)
    print(f"Base surface area of the square pyramid is {base_area} square feet.")

    side_area = calcSideArea(side, height)
    print(f"Side surface area of the square pyramid is {side_area} square feet")

    prntSurfArea(side, height)

if __name__ == "__main__":
    main()

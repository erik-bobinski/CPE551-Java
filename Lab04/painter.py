# Author: Erik Bobinski
# Date: 9/24/2024
# Description: A small description in your own words that describes what the program does.


def Intro():
    artInput = input("Welcome! Input [1-4] to choose your ASCII art to display. 1 is sailingShip, 2 is sleepingCat, 3 is aardvark, 4 is iysaur\n")
    borderInput = input("Input the single character you would like as the border for your art:\n")
    print(f"You chose {artInput} for your art, and {borderInput} as the border")

def PrintHeaderFooter(borderInput, size):
    for i in range(size):
        print("borderInput", end="")

def SleepingCat(borderInput):
    # 32 characters across
    sleepingCatArt =  

    #covers the top of the art
    PrintHeaderFooter(borderInput, 32)

    #some method to surround sides of art with borderInput
    
    #covers the bottom of the art
    PrintHeaderFooter(borderInput, 32)

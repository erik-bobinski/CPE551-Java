# Author: Erik Bobinski
# Date: 9/24/2024
# Description: All required functions for painterMain.py
# The functions introduce the user to program, displays desired ASCII art
# Intended to be exported for use in painterMain.py

# Takes user input and returns their art choice and border choice
def Intro():  
    """
    Takes input, returns user's choice of art and border
    :param artInput: user's choice of ASCII art
    :type artInput: string
    :param borderInput: user's choice of ASCII art border
    :type borderInput: string
    :return: user's art and border
    """
    artInput = input(
        "Welcome! Input [1-4] to choose your ASCII art to display. 1 is a Sleeping Cat, 2 is a Sailing Ship, 3 is an Aardvark, 4 is Iysaur:\t"
    )
    borderInput = input(
        "Input the single character you would like as the border for your art:\t"
    )
    return artInput, borderInput

# prints border char horizontally equal to width of ASCII image
def PrintHeaderFooter(borderInput, size):
    """
    Prints top and bottom of art border
    :param borderInput: user's choice of border
    :type borderInput: string
    :param artInput: user's choice of art
    :type artInput: string
    :return: void
    """
    print(borderInput * size)

def SleepingCat(borderInput):
    """
    Prints respective art
    :param borderInput: user's choice of border
    :type borderInput: string
    :return: void
    """

    # covers the top of the art
    PrintHeaderFooter(borderInput, 33)

    # reads each line of text image, inserts borderInput before and after each line
    with open("sleepingCat.txt", "r") as file:
        for line in file:
            if len(line.rstrip()) >= 30:
                print(
                    f"{borderInput}",
                    line.rstrip(),  # rstrip() removes trailing spaces
                    f"{borderInput}",
                )
            else:
                print(
                    f"{borderInput}",
                    line.rstrip(),
                    " " * (29 - len(line.rstrip())),  # rstrip() removes trailing spaces
                    f"{borderInput}",
                )

    # covers the bottom of the art
    PrintHeaderFooter(borderInput, 33)


def SailingShip(borderInput):
    """
    Prints respective art
    :param borderInput: user's choice of border
    :type borderInput: string
    :return: void
    """

    # covers the top of the art
    PrintHeaderFooter(borderInput, 30)

    # reads each line of text image, inserts borderInput before and after each line
    with open("sailingShip.txt", "r") as file:
        for line in file:
            if len(line.rstrip()) >= 29:
                print(
                    f"{borderInput}",
                    line.rstrip(),  # rstrip() removes trailing spaces
                    f"{borderInput}",
                )
            else:
                print(
                    f"{borderInput}",
                    line.rstrip(),
                    " " * (28 - len(line.rstrip())),  # rstrip() removes trailing spaces
                    f"{borderInput}",
                )

    # covers the bottom of the art
    PrintHeaderFooter(borderInput, 33)


def Aardvark(borderInput):
    """
    Prints respective art
    :param borderInput: user's choice of border
    :type borderInput: string
    :return: void
    """

    # covers the top of the art
    PrintHeaderFooter(borderInput, 55)

    # reads each line of text image, inserts borderInput before and after each line
    with open("aardvark.txt", "r") as file:
        for line in file:
            if len(line.rstrip()) >= 51:
                print(
                    f"{borderInput}",
                    line.rstrip(),  # rstrip() removes trailing spaces
                    f"{borderInput}",
                )
            else:
                print(
                    f"{borderInput}",
                    line.rstrip(),
                    " " * (50 - len(line.rstrip())),  # rstrip() removes trailing spaces
                    f"{borderInput}",
                )

    # covers the bottom of the art
    PrintHeaderFooter(borderInput, 55)


def Ivysaur(borderInput):
    """
    Prints respective art
    :param borderInput: user's choice of border
    :type borderInput: string
    :return: void
    """

    # covers the top of the art
    PrintHeaderFooter(borderInput, 72)

    # reads each line of text image, inserts borderInput before and after each line
    with open("ivysaur.txt", "r") as file:
        for line in file:
            if len(line.rstrip()) >= 68:
                print(
                    f"{borderInput}",
                    line.rstrip(),  # rstrip() removes trailing spaces
                    f"{borderInput}",
                )
            else:
                print(
                    f"{borderInput}",
                    line.rstrip(),
                    " " * (67 - len(line.rstrip())),  # rstrip() removes trailing spaces
                    f"{borderInput}",
                )

    # covers the bottom of the art
    PrintHeaderFooter(borderInput, 72)


def Blank(borderInput):
    """
    Prints blank canvas
    :param borderInput: user's choice of border
    :type borderInput: string
    :return: void
    """

    PrintHeaderFooter(borderInput, 14)

    for i in range(10):
        print(f"{borderInput}", " " * 10, f"{borderInput}")

    PrintHeaderFooter(borderInput, 14)

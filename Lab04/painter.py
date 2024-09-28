# Author: Erik Bobinski
# Date: 9/24/2024
# Description: A small description in your own words that describes what the program does.


# Takes user input and returns their art choice and border choice
def Intro():
    artInput = input(
        "Welcome! Input [1-4] to choose your ASCII art to display. 1 is a Sailing Ship, 2 is a Sleeping Cat, 3 is an Aardvark, 4 is Iysaur\t"
    )
    borderInput = input(
        "Input the single character you would like as the border for your art:\t"
    )
    return artInput, borderInput


# prints border char horizontally equal to width of ASCII image
def PrintHeaderFooter(borderInput, size):
    print(borderInput * size)


def SleepingCat(borderInput):
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
    PrintHeaderFooter(borderInput, 14)

    for i in range(10):
        print(f"{borderInput}", " " * 10, f"{borderInput}")

    PrintHeaderFooter(borderInput, 14)


def main():

    # take user input
    art, border = Intro()

    print(f"Art = {art}")

    # display user specified art
    if art == 1:
        SleepingCat(border)
    elif art == 2:
        SailingShip(border)
    elif art == 3:
        Aardvark(border)
    elif art == 4:
        Ivysaur(border)
    else:
        Blank(border)

    print("Enjoy your art :-)")


if __name__ == "__main__":
    main()

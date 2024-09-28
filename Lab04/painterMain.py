# Author: Erik Bobinski
# Date: 9/24/2024
# Description: Main function for painter program. Imports dependencies from painterFuncs.py,
# takes in user input, displays desired ASCII art, then program terminates


import painterFuncs as pf

def main():
    # take user input
    art, border = pf.Intro()

    # must be int for value comparison
    art = int(art)

    # display user specified art
    if art == 1:
        pf.SleepingCat(border)
    elif art == 2:
        pf.SailingShip(border)
    elif art == 3:
        pf.Aardvark(border)
    elif art == 4:
        pf.Ivysaur(border)
    else:
        pf.Blank(border)

    print("Enjoy your art :-)")


if __name__ == "__main__":
    main()

# Author: Erik Bobinski
# Date: 9/18/2024
# Description: Three attemps to guess a particle's coordinates 
# within range of [1,10], and some info after each attempt
userGuesses = 3
xPos = 5
yPos = 3

while(1):
    print(f"\nYou have {userGuesses} attemps remaining\n")

    if userGuesses == 0:
        print(f"You lost! The coordinates were ({xPos}, {yPos})")
        break
    
    # handle x input
    guessX = input("Guess the particles x position[1-10]: ")
    while(guessX.isdigit() == False or int(guessX) < 1 or int(guessX) > 10):
        guessX = input("Guess the particle's x position, must be integer [1-10]: ")
    guessX = int(guessX)

    # handle y input
    guessY = input("Guess the particles y position[1-10]: ")
    while(guessY.isdigit() == False or int(guessY) < 1 or int(guessY) > 10):
        guessY = input("Guess the particle's y position, must be integer [1-10]: ")
    guessY = int(guessY)

    # guess validation 
    if guessX == xPos and guessY == yPos:
        print("You guessed the particle's position correctly!")
        break
    if guessX < xPos:
        print("\nYour x position guess was less than the actual")
    else:
        print("\nYour x position guess was greater than the actual")
    if guessY < yPos:
        print("Your y position guess was less than the actual")
    else:
        print("Your y position was greater than the actual")
    userGuesses -= 1



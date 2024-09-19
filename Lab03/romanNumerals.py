# Author: Erik Bobinski
# Date: 9/18/2024
# Description: Converts user specified number in the range of 1-9 inclusively,
# equivalent Roman numeral according to a unicode table

# Handle user input
userInput = input("Input a number between 1 and 9: ")
while( userInput.isdigit() == False or int(userInput) < 1 or int(userInput) > 9 ):
    userInput = input("Input a number between 1 and 9: ")
userInput = int(userInput)

# Handle roman numeral conversion


 

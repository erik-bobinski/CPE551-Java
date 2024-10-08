# Author: Erik Bobinski
# Date: 9/18/2024
# Description: Converts user specified number in the range of 1-9 inclusively,
# equivalent Roman numeral according to a unicode table

# Handle user input
userInput = input("Input a number between 1 and 9 inclusive: ")
while not userInput.isdigit() or int(userInput) < 1 or int(userInput) > 9:
    print("\tYou can only input an integer, try again.\n")
    userInput = input("Input a number between 1 and 9: ")
userInput = int(userInput)

# Handle roman numeral conversion
if userInput == 1:
    print(f"{userInput} in roman numerals is \u2160")
elif userInput == 2:
    print(f"{userInput} in roman numerals is \u2161")
elif userInput == 3:
    print(f"{userInput} in roman numerals is \u2162")
elif userInput == 4:
    print(f"{userInput} in roman numerals is \u2163")
elif userInput == 5:
    print(f"{userInput} in roman numerals is \u2164")
elif userInput == 6:
    print(f"{userInput} in roman numerals is \u2165")
elif userInput == 7:
    print(f"{userInput} in roman numerals is \u2166")
elif userInput == 8:
    print(f"{userInput} in roman numerals is \u2167")
elif userInput == 9:
    print(f"{userInput} in roman numerals is \u2168")
else:
    print("Logic error occurred")

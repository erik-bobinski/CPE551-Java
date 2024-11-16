# Erik Bobinski
# 11/16/2024
# This program checks if a series of parentheses entered by the user is balanced 
# using a recursive function to evaluate the input

count = 0

def parenTest(line, position):
    """
    Recursive function to determine if the parentheses in a string are balanced.
    :param line: String of '(' and ')' characters
    :param position: Current position in the string
    :return: Boolean indicating whether the parentheses are balanced
    """
    global count
    
    if position == len(line):
        return count == 0  # Balanced if count is 0
    
    if line[position] == '(':
        count += 1
    elif line[position] == ')':
        count -= 1
    
    # If count goes negative, it means there's an unmatched ')'
    if count < 0:
        return False
    
    # Recursive case: Move to the next position
    return parenTest(line, position + 1)

def main():
    """
    Main function to get user input and check for balanced parentheses.
    """
    global count
    user_input = input("Enter a series of '(' and ')' characters: ")
    
    # Reset count before checking a new string
    count = 0
    is_balanced = parenTest(user_input, 0)
    
    if is_balanced:
        print("The series of parentheses is balanced.")
    else:
        print("The series of parentheses is not balanced.")

if __name__ == "__main__":
    main()
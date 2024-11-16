# Erik Bobinski
# 11/16/2024
# This program checks whether a given word is a palindrome using a recursive function.

def palinTest(word):
    """
    Recursive function to determine if a word is a palindrome.
    :param word: The string to be tested
    :return: Boolean indicating whether the word is a palindrome
    """
    # Base case: A single character or an empty string is always a palindrome
    if len(word) == 0 or len(word) == 1:
        return True

    # If the first and last characters are not the same, not a palindrome
    if word[0] != word[-1]:
        return False
    
    # Recursive case: Check the remaining substring
    return palinTest(word[1:-1]) 
        
def main():
    """
    Main function to get user input and check if the word is a palindrome.
    """
    word = input("Enter a word to test if it's a palindrome: ")
    if palinTest(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome!")

if __name__ == "__main__":
    main()
# Erik Bobinski
# 11/16/2024
# This program checks whether a given word is a palindrome using an iterative approach.

def palinTest(word):
    """
    Iterative function to determine if a word is a palindrome.
    :param word: The string to be tested
    :return: Boolean indicating whether the word is a palindrome
    """
    l = 0
    r = len(word) - 1
    
    # Iterate over the word to compare characters from both ends
    for i in range(len(word)):
        if word[l] != word[r]:
            return False
        
        # If the pointers meet or cross, the word is a palindrome
        if l == r or l > r:
            return True
        l += 1
        r -= 1
        
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
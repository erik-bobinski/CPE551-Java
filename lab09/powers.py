# Erik Bobinski
# 11/16/2024
# This program calculates the result of raising a base to an exponent using recursion.

def powers(base, exp):
    """
    Recursive function to compute the power of a base raised to an exponent.
    :param base: The base value (float)
    :param exp: The exponent value (integer)
    :return: The result of base raised to the power of exp
    """
    print(f"powers({base}, {exp})")

    # Base case: When exponent is 1, return the base
    if exp == 1:
        return base
    
    # Recursive case: Multiply the base by the result of base^(exp-1)
    return base * powers(base, exp - 1)

def main():
    """
    Main function to prompt the user for base and exponent values,
    calculate the result using the powers function, and display the output.
    """
    senti = True
    while senti:
        try:
            base = float(input("Input the value for the base (any number): "))
            exp = int(input("Input the value for the exponent (any integer): "))
        except ValueError:
            print("Must enter numbers, specifically an integer for the exponent!")
        else:
            res = powers(base, exp)
            print(f"Result of {base} raised to {exp} is {res}")
            senti = False

if __name__ == "__main__":
    main()
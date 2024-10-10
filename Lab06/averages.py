import os

def average(file):
    """
    Calcs the avg of integers in a file
    :param file: user file input
    :type file: string
    :return: float avg of integers from file 
    """
    avg = 0.0
    n = 0 # denominator for avg
    sum = 0 # numerator for avg

    #check if file exists
    if os.path.exists(file):
        with open(file) as myFile: # r is default mode  
            for line in myFile: # parse and process each line
                sum += int( line.strip() )
                n += 1
                avg = sum / n
                print(f"processing line: {line.strip()}...")
        return avg
    else:
        print(f"{file} was not found!")
        return avg


def main():
    file = "user-input-here"
    senti = True # sentinel value

    # user input loop
    while senti:
        file = input("Input the name of the file whose contents you want to average (include file extension!): ")
        avg = average(file)    
        choice = input("Do you want to calculate the average using this file? (\"y\" to finish, \"n\" to try again): ")
        if choice.lower() == "y":
            senti = False

    print(f"The average value rounded to the nearest hundredth is {avg:.2f}!") 


if __name__ == "__main__":
    main()

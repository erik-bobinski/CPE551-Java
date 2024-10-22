import os

def getFileName() -> str:
    """
    Retrieves fileName from user
    :return: string 
    """
    while True:
        fileName = input("Input the name of the csv file you want to convert to symbols: ")
        if os.path.exists(fileName):
            break
        else:
            print("File does not exist in this directory, try again.")
    return fileName

def convertLine(line) -> str:
    """
    converts integers in file from numbers to symbols
    :param line: single line of file, contains integers delimited by commas
    :type line: string
    :return: string 
    """
    # split string into a list delimited by commas
    line = line.strip().split(",")

    # convert numbers into symbols
    newLine = ""
    for i in range(len(line)):
        if line[i] == "1":
            newLine += " "
        elif line[i] == "2":
            newLine += ","
        elif line[i] == "3":
            newLine += "_"
        elif line[i] == "4":
            newLine += "("
        elif line[i] == "5":
            newLine += "O"
        elif line[i] == "6":
            newLine += ")"
        elif line[i] == "7":
            newLine += "-"
        elif line[i] == "8":
            newLine += "\""

    return newLine

def processFile(filename):
    """
    Reads input file, converts each line of integers to symbols and prints to output file
    :param filename: User input file to be processed
    :type filename: string
    :return: void 
    """
    # parse input file and write to output file
    with open(filename) as fileInput:
        with open("painting.txt", "w") as fileOutput:
            for lineInput in fileInput:
                lineOutput = convertLine(lineInput)
                fileOutput.write(f"{lineOutput}\n")


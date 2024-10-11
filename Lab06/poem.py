import os

def main():

    # input validation
    while True: 
        file = input("Enter the name of the file you want to read: ")
        if os.path.exists(file):
            break
        choice = input("File doesn't exist, try again?(y/n): ")
        if choice.lower() != "y":
            exit() 

    # parse and extract file        
    with open(file) as pFile:
        title = pFile.readline()
        author = pFile.readline()
        lines = [line for line in pFile]


    # write to output file
    with open("Output.txt", "w") as out:
        out.write(f"Title: {title}") 
        out.write(f"Author: {author}") 
        out.write(f"This poem has {len(lines)} lines, below is a preview:\n\n")
        out.writelines(lines[0:3])
        out.write("...")

if __name__ == "__main__":
    main()

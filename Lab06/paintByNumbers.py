import pbnFunctions as pbn

def main():
    pbn.processFile( pbn.getFileName() )
    print("Your output file is located in \"painting.txt\"!")

if __name__ == "__main__":
    main()

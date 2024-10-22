import os # validate file existence

from typing import Dict, Set, Tuple # to specify return types -> type safety and paramter organization

# stying
italic = "\033[3m"
reset = "\033[0m"

def LoadBooks() -> Tuple[Dict[str, list[str]], Set[str]]:
    """
    Reads in csv file of book data, returns dict of data and set of categories
    :return: Tuple containing dictionary of books, and set of categories
    """

    books = {} # key: book title, value: data
    categories = set() # tracks categories for books
    
    while True:
        # specify path to target file
        projectDir = os.path.dirname(os.path.abspath(__file__))
        sampleDir = os.path.join(projectDir, "SampleInputOutput")
        bookFile = os.path.join(sampleDir, input("Input the csv file containing book information: ")) # finalized path
        
        # check file existence and parse
        if os.path.exists(bookFile):
            with open(bookFile, "r") as file:
                next(file) # skip first line (header line)
                for line in file:
                    lineList = line.strip().split(",") # break line into comma-delimited list
                    books[lineList[0]] = lineList[1:] # book title as key, remaining data as value
                    categories.add( lineList[-1].lower() ) # add category(last list-item) to set 
            break
        else:
            print("File not found.\n")
    
    return books, categories



def LoadReviews(books: Dict[ str, list[str] ]) -> list[str]:
    """
    Reads in csv file to extract book review data, returns list of book review data 
    
    :param books: contains book titles and corresponding data
    :param type: Dict[ str, list[str] ]

    :return: list of reviews of books found in book dictionary
    """

    # result list to build
    bookReviews = [] 
    
    while True:
        # specify path to target file
        projectDir = os.path.dirname(os.path.abspath(__file__))
        sampleDir = os.path.join(projectDir, "SampleInputOutput")
        reviewFile = os.path.join(sampleDir, input("\nInput the csv file containing book review information: ")) # finalized path

        
        #check file existence and parse
        if os.path.exists(reviewFile):
            with open(reviewFile, "r") as file:
                next(file) # skip first line (header line)
                for line in file:
                    lineList = line.strip().split(",") # break line into comma-delimited list

                    try:
                        # check if title in dict
                        if lineList[1] in books:
                            # add review to list of reviews
                            bookReviews.append(lineList)    
                        else:
                            raise LookupError(f"{lineList[1]} not found in books dictionary")

                    except LookupError: 
                        print(LookupError)
                break
        else:
            print("File not found.")

    return bookReviews



def BooksFromCategory(books: Dict[str, list[str]], categories: Set[str]) -> None:
    """
    Outputs all books from user-specified category

    :param books: dictionary containing books and their data 
    :param type: Dict[str, list[str]]

    :param categories: set of unique categories from all books
    :param type: Set[str]

    :return: None
    """
    # list conversion of categories-set, for easier traversal 
    categoriesList = list(categories)

    userCategory = ""

    # user input must exist in categories and be of type int
    while not isinstance(userCategory, int):

        # Display all categories for user to choose from
        print("\nBelow are all book categories:")
        for i in range(len(categoriesList)):
            print(f"\t{i+1}. {categoriesList[i]}")

        # error-handle user input
        try:
            userCategory = int( input(f"\nWhich category would you like to see? (1 - {len(categoriesList)}): ") ) 
        except:
            print("You must input an integer within the specified bounds!")

    print(f"{categoriesList[userCategory - 1]} books:")

    for title in books:
        # if book has the user specified category
        if books[title][-1].lower() == categoriesList[userCategory - 1]:
            print(f"\t{italic}{title}{reset}, by {books[title][1]}\n") # title is dict key, index 1 is author



def BookData(books: Dict[str, list[str]], bookReviews: list[str]) -> None:
    """
    Choose a book to output all its data

    :param books: collection of all books
    :param type: Dict[str, list[str]]

    :param bookReviews: list of all book reviews
    :param type: list[str]

    :return: None
    """
    booksList = [] # list of book titles
    userIndex = "" 

    # ensure user-chosen book exists and is inputted as integer from a list
    while not isinstance(userIndex, int):

        # build booksList and show titles to user
        print("\nHere are all available book titles:")
        count = 1
        for title in books:
            print(f"\t{count}. {italic}{title}{reset}")
            booksList.append(title)
            count += 1

        try:
            userIndex = int( input(f"\nWhich book would you like to see?(1 - {count - 1}): " ) ) # 1-index of booksList
        except:
            print("You must input an integer within the above bounds!")
            userIndex = ""
            continue
        
        if booksList[userIndex - 1] not in books:
            print("Book not found!")
            userIndex = ""
            continue

    #scan review list for ratings and pricings of user-chosen book
    userBook = booksList[userIndex - 1] # title of user-chosen book
    priceSum = 0
    ratingSum = 0
    bookCount = 0
    for line in bookReviews:
        if line[1] == userBook:
            priceSum += float(line[2]) 
            ratingSum += float(line[-1])
            bookCount += 1

    # calc averages if a review exists
    if bookCount != 0:
        priceAvg = priceSum / bookCount
        ratingAvg = ratingSum / bookCount
        priceAvg = round(priceAvg, 2)
        ratingAvg = round(ratingAvg, 1)

    #output detailed info on userBook
    print(f"\nMore information on {italic}{userBook}{reset}:")
    print(f"\tDescription: ", end="")
    print("-\n\t".join([books[userBook][0][i:i+60] for i in range(0, len(books[userBook][0]), 60)]))  # Breaks every 60 characters
    print(f"\n\tPublished by: {books[userBook][2]}, {books[userBook][3]}")
    print(f"\n\tCategory: {books[userBook][-1]}")
    if bookCount != 0: # if user-chosen book has reviews
        print(f"\n\tAverage price: ${priceAvg}")
        print(f"\n\tAverage rating: {ratingAvg} / 5.0\n")
    else:
        print("\n\tNo price listings nor reviews available\n")



def AuthorRatings(books: Dict[str, list[str]], bookReviews: list[str]) -> None: 
    """
    Outputs the average rating for each author from bookReviews file

    :param books: collection of all books
    :param type: Dict[str, list[str]]

    :param bookReviews: list of all book reviews
    :param type: list[str]

    :return: None
    """
    # build dict of {authors:their book titles} using books dict
    authorBooks = {}

    # add each author and their title's from books to authorBooks
    for title in books:
        
        # handle case of multiple authors for one book
        authors = books[title][1].split(";")
        
        for author in authors:

            # if author not in authorBooks, initialize the author
            if author not in authorBooks:
                authorBooks[author] = [title]        

            # else add new title to the author
            else:
                authorBooks[author].append(title) 

    # determine average rating of each author using authorBooks and bookReviews 
    authorRating = {} # dict {author:average rating}

    for author in authorBooks:
        ratingSum = 0.0
        ratingCount = 0

        for review in bookReviews:

            for book in authorBooks[author]:
                
                if book in review:
                    ratingCount += 1 # increment amount of ratings for the author
                    ratingSum += float(review[-1]) # add rating to total
                    authorRating[author] = ratingSum / ratingCount # insert latest average for author
        if ratingCount == 0:
            authorRating[author] = "N/A"


    # print result
    print(f"\nEach author and their average ratings:")
    for author in authorRating:
        if authorRating[author] != "N/A":
            print(f"\n\t{author}: {float(authorRating[author]):.2f}")
        else:
            print(f"\n\t{author}: No ratings")


def HelpfulReviewer(bookReviews: list[str]) -> None:
    """
    Outputs the name and average helpfulness rating of the most helpful reviewer

    :param bookReviews: list of all book reviews
    :param type: list[str]

    :return: None
    """
    
    # create dict {reviewer:helpfulness[numerator, denominator]}
    # numerator = amount of ratings that stated a reviewer was helpful
    # denominator = total amount of ratings of a reviewer
    revRatings = {} 

    for review in bookReviews:

        reviewer = review[4]

        # convert helpfulness ratings into list of ints for analysis
        # [0] = numerator, [1] = denominator
        helpRating = review[-2].split("/")
        helpRating = [int(num) for num in helpRating]
    
        # sum up total helpfulness ratings
        if reviewer not in revRatings:
            revRatings[reviewer] = helpRating
        else:
            # add the two fractions
            revRatings[reviewer] = [num + denom for num, denom in zip(revRatings[reviewer], helpRating)]
            revRatings[reviewer][1] += helpRating[1]


    # find most helpful reviewer by iterating thru revRatings{reviewer: [num, denom]}

    # attributes of most helpful reviewer
    maxNumer = 0
    maxDenom = 0
    maxName = "" 

    for reviewer in revRatings:
        numer = revRatings[reviewer][0] # amount of meta-ratings that stated helpful
        denom = revRatings[reviewer][1] # total amount of meta-ratings

        # only consider reviewers with at least 10 meta-ratings
        if denom > 10:
            
            # we found a new most helpful reviewer
            if numer > maxNumer:
                maxNumer = numer
                maxDenom = denom
                maxName = reviewer 

    # print result
    maxAvg = int(maxNumer / maxDenom * 100)
    print(f"\nMost helpful reviewer: {maxName}\nAverage Helpfulness Rating: {maxAvg}%\n")



def Welcome() -> None:
    print("Welcome to Book Mobile :^)\n")



def Goodbye() -> None:
    print("Goodbye -.-")



def Menu() -> int:
    num = ""
    while not isinstance(num, int): 

        try:
            num = int( input(
                "\nWhich option would you like to choose? (1 - 7)\n"
                "1. Load Book File\n"
                "2. Load Book Review File\n"
                "3. Show Books by Literary Category\n"
                "4. Show Book's Details\n"
                "5. Show Average Author Ratings\n"
                "6. Most Helpful Reviewer\n"
                "7. Quit\n\n") )
        except:
            print("\nEnter an integer [1-7]")

    return num 

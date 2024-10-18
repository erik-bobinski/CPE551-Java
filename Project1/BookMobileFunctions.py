from os.path import exists # validate file existence
from typing import Dict, Set, Tuple # to specify return types - type safety and paramter organization

def LoadBooks() -> Tuple[ Dict[str, list[str]], Set[str] ]:
    """
    Reads in csv file to extract book data, returns dictionary of data, and set of book categories

    :return: Tuple containing dictionary of books, and set of categories
    """

    books = {} # key: book title, value: data
    categories = set() # tracks categories for books
    bookFile = input("Input the csv file containing book information: ")

    while True:

        # check file existence and parse 
        if exists(bookFile):
            with open(bookFile, "r") as file:
                next(file) # skip first line (header line)
                for line in file:
                    lineList = line.strip().split(",") # break line into comma-delimited list
                    books[lineList[0]] = lineList[1:] # book title as key, remaining data as value
                    categories.add( lineList[-1].lower() ) # add category(last list item) to set 
            break
        bookFile = input("File not found. Input the csv file containing book information: ")
    
    return books, categories



def LoadReviews(books: Dict[ str, list[str] ]) -> list[str]:
    """
    Reads in csv file to extract book review data, returns list of book reviews 
    
    :param books: contains book titles and corresponding data
    :param type: Dict[ str, list[str] ]

    :return: list of reviews of books found in book dictionary
    """

    # list of book reviews that exist in book dict
    bookReviews = [] 
    
    reviewFile = input("Input the csv file of the book reviews: ")

    while True:
        
        #check file existence and parse
        if exists(reviewFile):
            with open(reviewFile, "r") as file:
                for line in file:
                    next(file) # skip first line (header line)
                    lineList = line.strip().split(",") # break line into comma-delimited list

                    try:
                        # check if book is in dictionary
                        if lineList[1] in books:
                            # add book's review to list of reviews
                            bookReviews.append(lineList[5])    
                        else:
                            raise LookupError(f"{lineList[1]} not found in books dictionary")

                    except LookupError: 
                        print(LookupError)
            break
        reviewFile = input("File not found. Input the csv file of the book reviews: ")

    return bookReviews



def BooksFromCategory(books: Dict[ str, list[str] ], categories: Set[str]) -> None:
    """
    Outputs all books from user-specified category

    :param books: dictionary containing books and their data 
    :param type: Dict[str, list[str]]

    :param categories: set of unique categories from all books
    :param type: Set[str]

    :return: None
    """
    
    userCategory = ""

    # input must exist in categories and be of type int
    while userCategory not in categories or not isinstance(userCategory, int):

        # Display all categories for user to choose from
        print("Below are all book categories:")
        count = 1 # index of categories set
        for category in categories:
            print(f"{count}. {category}")
            count += 1
        userCategory = input(f"\nWhich category would you like? (1 - {len(categories)})") 

    print(f"Each book below is of the {userCategory} category.")

    for title in books:
        # if book has that userCategory
        if books[title][len(books[title]) - 1] == userCategory:
            print(f"\tTitle: \"{title}\"\tAuthor: {books[title][1]}") # title is dict key, index 1 is author



def BookData(book: Dict[str, list[str]], bookReviews: list[str]):

    # function instructions on end of page 2 of project instructions 
    # debug prev functions before writing this one
    """
    Choose a book to output all its data

    :param book: collection of all books
    :param type: Dict[str, list[str]]

    :param bookReviews: list of all book reviews
    :param type: list[str]

    :return: None
    """

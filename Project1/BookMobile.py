import BookMobileFunctions as bmf


def main():
    
    isFilesLoaded = False

    bmf.Welcome()


    while True:

        choice = bmf.Menu()

        match choice:

            case 1:
                bookDict, categoriesSet = bmf.LoadBooks()
                isFilesLoaded = True

            case 2:
                if not isFilesLoaded:
                    print("You need to load Book Files!\n")
                else:
                    try:
                        reviewList = bmf.LoadReviews(bookDict)
                        isFilesLoaded = True
                    except LookupError:
                        print("File does not exist!\n")

            case 3:
                if not isFilesLoaded:
                    print("You need to load Book Files!\n")
                else:
                    bmf.BooksFromCategory(bookDict, categoriesSet)

            case 4:
                if not isFilesLoaded:
                    print("You need to load Book Files!\n")
                else:
                    bmf.BookData(bookDict, reviewList)

            case 5:
                if not isFilesLoaded:
                    print("You need to load Book Files!\n")
                else:
                    bmf.AuthorRatings(bookDict, reviewList)

            case 6:
                if not isFilesLoaded:
                    print("You need to load Book Files!\n")
                else:
                    bmf.HelpfulReviewer(reviewList)

            case 7:
                exit()

            case _:
                print("Invalid option, choose between [1-7]")

    #bookDict, categoriesSet = bmf.LoadBooks() 

    #reviewList = bmf.LoadReviews(bookDict) 

    #bmf.BooksFromCategory(bookDict, categoriesSet)

    #bmf.BookData(bookDict, reviewList)

    #bmf.AuthorRatings(bookDict, reviewList)

    #bmf.HelpfulReviewer(reviewList)


if __name__ == "__main__":
    main()

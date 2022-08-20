bookList = []

books = open('bookstock.txt', 'r') #opens the text document in read mode

for eachline in books:
    eachline = eachline + "\n"
    book_details = []
    start_pos = 0
    if not eachline.startswith('#'):
        for index in range(len(eachline)):
            if eachline[index] == ',' or index == len(eachline) -1:
                book_details.append(eachline[start_pos:index].strip())
                start_pos = index + 2

        bookList.append(book_details) #this block of code assigns the .txt file to a list called 'bookList'



books.close()

def menu():
    option=int(input("==========================================" #beginning of text that makes up the main menu
                     "\n1) = Report of the book titles."
                     "\n2) = Average price."
                     "\n3) = Books in each genre."
                     "\n4) = Add a new book."
                     "\n5) = Check availability."
                     "\n6) = Orderised Books."
                     "\n7) = Exit application."
                     "\n=========================================="
                     "\n\nChoose a menu option: "))                 #end of text that makes up the main menu
    if option == 1:                     #this is the start of the loop that calls the other functions when the user enters their choice
        List()
    elif option == 2:
        avgPrice()
    elif option == 3:
        NumberOfGenre()
    elif option == 4:
        NewBook()
    elif option == 5:
        Availability()
    elif option == 6:
        BooksInOrder()
    elif option == 7:
        Close()

def List():
       
    for eachline in bookList:
        print (eachline)

    bookStock = 0
    bookValue = 0 
    for eachline in bookList:
        stockLevel = int(eachline[5])   #this assigns the variable stockLevel to the stock within the list
        if stockLevel > 0:
            bookValue = bookValue + (float(eachline[4])) * (float(eachline[5]))
            bookStock = bookStock + 1                                               #moves onto the next book in the list

    print('\n The number of titles available is: ' , len(bookList))
    print('\n The total cost of the books is: £' , round(bookValue, 2) , sep= ' ' )
    menu()
        
       

def avgPrice():

    bookStock = 0
    bookValue = 0
    avgPrice = 0

    for eachline in bookList:
        stockLevel = int(eachline[5])
        if stockLevel > 0:
            bookValue = bookValue + (float(eachline[4]))
            bookStock = bookStock + 1
            avgPrice = bookValue / len(bookList)    #this line of code divides the assigned variable 'bookStock' by the length of the book list
            
    print('The average price of the books is £', round(avgPrice, 2) , sep= ' '  )
    menu()



def NumberOfGenre(): 
    genre = ''
    ficNum = 0
    bioNum = 0
    relNum = 0
    sciNum = 0

    for eachline in bookList:
        if eachline[6] =='fiction':
            ficNum += 1
        elif eachline[6] =='biography':
            bioNum += 1
        elif eachline[6] =='religion':
            relNum += 1
        elif eachline[6] =='science':
            sciNum += 1

    print('There is ' ,ficNum, ' Fiction books.')
    print('There is ' ,bioNum, ' Biography books.')
    print('There is ' ,relNum, ' Religion books.')
    print('There is ' ,sciNum, ' Science books.')
    menu()



def NewBook():

    author = input("Author: ")
    title = input("Title: ")
    format = input("Format: ")
    publisher = input("Publisher: ")
    price = input("Price: ")
    stock = input("Stock: ")
    genre = input("Genre: ")

    newBook = author, title, format, publisher, price, stock, genre
    bookList.append(newBook)

    bookStock = 0
    bookValue = 0
    avgPrice = 0

    for eachline in bookList:
        stockLevel = int(eachline[5])
        if stockLevel > 0:
            bookValue = bookValue + (float(eachline[4]))
            bookStock = bookStock + 1
            avgPrice = bookValue / len(bookList)

    avgPriceDiff = avgPrice - 18.17

    print('\nThe number of titles available is now: ' , len(bookList))
    print('The average price of the books is: £', round(avgPrice, 2) , sep= ' '  )
    print('The average price difference of the books is: £', round(avgPriceDiff, 2) , sep= ' '  )

    menu()


def Availability():

    queryBook = input('Enter the title of book: ')
    for eachline in bookList:   
        
        if eachline[1].lower() == queryBook.lower():
            print('The stock levels of that book are ' , eachline[5])
            userOption = int (input('Would you like to [1] Increase or [2] Decrease the stock levels? Key in [3] if you would like to return to the menu.'))
            stockLevel = int(eachline[5])

            if userOption == 1:
                increaseAmount = int(input('How much would you like to increase the stock level by?'))
                stockLevel = stockLevel + increaseAmount
                print('The new stock level is now ' ,stockLevel)
                
                menuOption= input()
            elif userOption ==2:
                decreaseAmount = int(input('How much would you like to increase the stock level by?'))
                stockLevel = stockLevel - decreaseAmount
                if stockLevel <= 0:
                    print('This book is now out of stock.')
                elif stockLevel > 0:
                    print('The new stock level is now ' ,stockLevel)
            elif userOption == 3:
                menuAnswer = input('Would you like to return to the main menu or go back? [1] for go back or [2] for main menu')
                if menuAnswer == 1:
                   Availability()
                
                elif userOption ==2:
                    menu()
    menu()


def BooksInOrder():

    sortOption = int(input('What would you like to sort by? [1] for Title or [2] for Genre'))
    if sortOption == 1:
        titleList = []
        for eachline in bookList:
            titleList.append([eachline[1] , eachline])
        sortedtitleList = sorted(titleList)
        for eachline in sortedtitleList:
            print(eachline[0])

    if sortOption == 2:
        genreList = []
        for eachline in bookList:
            genreList.append([eachline[1] , eachline])
        sortedgenreList = sorted(genreList)
        for eachline in sortedgenreList:
            print(eachline[0])
    menu()
            


def Close():
    exit()


menu()


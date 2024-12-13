import ReturnBook
import addbook
import lendBook
import loadBook
import removeBook
import updateBooks
import viewFile
books = loadBook.loadBook()

while True:
    print('----------------------------')
    print('Library Management System ')
    print('----------------------------')
    print('0. Exit')
    print('1. Add Book')
    print('2. View All Books')
    print('3. Update Books')
    print('4. Remove Books')
    print('5. Lend Books')
    print('6. Return Books')
    print('7. View Borrowers')
    op = input('Select your option : ')
    if op == '0':
        print('Thanks for using Library Management System')
        break
    elif op == '1':
        books = addbook.addbook(books)
    elif op == '2':
        viewFile.viewBook(books)
    elif op == '3':
        books = updateBooks.updateBooks(books)
    elif op == '4':
        books = removeBook.removeBooks(books)
    elif op == '5':
        books = lendBook.lendBooks(books)
    elif op == '6':
        ReturnBook.returnBook(books)
    elif op == '7':
        viewFile.viewBorrowers()
    else:
        print('Invalid Selection. Please try again ..!')

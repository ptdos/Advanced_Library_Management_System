import datetime

import savebook
import viewFile


def lendBooks(books):
    if len(books) == 0:
        print('Please add book first .....')
        return books
    availableBook = []
    for book in books:
        if book['quantity'] > 0:
            availableBook.append(book)
    if len(availableBook) == 0:
        print("There are not enough books available to lend.")
    else:
        viewFile.viewBook(availableBook)

        while True:
            try:
                index = int(input('Which number book you want to Lend :'))
                break
            except Exception as e:
                print(f'Error : {e}')

        try:
            print("Selected book : ")
            print(availableBook[index-1])
            check = input('Are you sure y/n :')
            if check.lower() == 'y':
                book_name = availableBook[index-1]['name']
                for book in books:
                    if book['name'] == book_name:
                        book['quantity'] -= 1
                        break
                name = input('Enter Your name : ')
                number = input('Enter Your Number : ')
                dueDate = (datetime.datetime.now()+datetime.timedelta(10)).strftime('%d / %m / %Y')
                user = [name, number, dueDate, book_name]
                savebook.borrower(user)
                savebook.savebook(books)
                print("Book Lend Successfully !!!")

            return books
        except Exception as e:
            print(f'Error : {e}')
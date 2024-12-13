import random
import datetime
import savebook


def addbook(books):
    name = input('Enter title of the book : ')
    author = input('Enter author name of the book : ')
    isbn = random.randint(1, 10000)
    while True:
        try:
            publishing_year = int(input('Publish year :'))
            break
        except Exception as e:
            print(f'Error : {e}')
    while True:
        try:
            price = int(input('Enter price :'))
            break
        except Exception as e:
            print(f'Error : {e}')
    while True:
        try:
            quantity = int(input('Enter Quantity :'))
            break
        except Exception as e:
            print(f'Error : {e}')
    addTime = datetime.datetime.now().strftime("%d / %m / %Y %H:%M:%S")

    book = {
        'name': name,
        'author': author,
        'isbn': isbn,
        'publishing_year': publishing_year,
        'price': price,
        'quantity': quantity,
        'addTime': addTime,
        'lastUpdate': ""
    }
    books.append(book)
    savebook.savebook(books)
    print('Book added successfully !!!')
    return books

import savebook
import viewFile
import datetime


def updateBooks(books):
    viewFile.viewBook(books)
    if len(books) == 0:
        print('Please add book first .....')
        return books
    while True:
        try:

            index = int(input('Which number book you want to update :'))
            break
        except Exception as e:
            print(f'Error : {e}')

    try:
        print("Selected book : ")
        print(books[index-1])
        print("----Please Enter Updated information--- ")
        name = input('Enter title of the book : ')
        author = input('Enter author name of the book : ')
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

        books[index-1]['name'] = name
        books[index-1]['author'] = author
        books[index-1]['publishing_year'] = publishing_year
        books[index-1]['price'] = price
        books[index-1]['quantity'] = quantity
        books[index-1]['lastUpdate'] = datetime.datetime.now().strftime("%d / %m / %Y %H:%M:%S")
        savebook.savebook(books)
        print('Book Update Successfully !!!')
        return books

    except Exception as e:
        print(f'Error : {e}')
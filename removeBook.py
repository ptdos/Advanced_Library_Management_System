import savebook
import viewFile


def removeBooks(books):
    viewFile.viewBook(books)
    if len(books) == 0:
        print('Please add book first .....')
        return books
    while True:
        try:
            index = int(input('Which number book you want to Remove :'))
            break
        except Exception as e:
            print(f'Error : {e}')

    try:
        print("Selected book : ")
        print(books[index - 1])
        check = input('Are you sure y/n :')
        if check.lower() == 'y':
            books.pop(index - 1)
            savebook.savebook(books)
            print("Book Remove Successfully !!!")

    except Exception as e:
        print(f'Error : {e}')
    return books

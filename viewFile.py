import csv


def viewBook(books):
    if len(books) == 0:
        print('No book found !!!')
    else:
        print("--------- All Book List ---------")
        for i in range(0, len(books)):
            print(f'{i+1} : {books[i]}')


def viewBorrowers():
    try:
        print("----All Borrowers--------")
        with open('borrower.csv', 'r') as file:
            csvFile = csv.reader(file)
            for user in csvFile:
                if len(user)>0:
                    print(user)
    except Exception as e:
        print(f'No data found !!')
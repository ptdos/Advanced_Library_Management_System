import csv
import json


def savebook(books):
    try:
        with open('books.json', 'w') as fp:
            json.dump(books, fp, indent=4)
    except Exception as e:
        print(f'Error : {e}')


def borrower(borrow):
    try:
        with open('borrower.csv', 'a', newline='') as file:
            csvFile = csv.writer(file)
            csvFile.writerow(borrow)
    except Exception as e:
        print(f'Error : {e}')

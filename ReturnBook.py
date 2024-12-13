import csv

import savebook


def returnBook(books):
    try:
        name = input("Enter Your name :")
        number = input("Enter Your Number :")
        with open('borrower.csv', 'r') as file:
            csvFile = csv.reader(file)
            user = []
            check = False
            for data in csvFile:
                if data[0] == name and data[1] == number:
                    bookName = data[3]
                    for book in books:
                        if book['name'] == bookName:
                            book['quantity'] += 1
                            savebook.savebook(books)
                            check = True
                            break
                else:
                    user.append(data)

            with open('borrower.csv', 'w', newline='') as myFIle:
                csvFile = csv.writer(myFIle)
                csvFile.writerows(user)
            if check:
                print('Return Successfully ')
            else:
                print('Your Information Not found !!!')
            return books
    except Exception as e:
        print(f"Error : {e}")
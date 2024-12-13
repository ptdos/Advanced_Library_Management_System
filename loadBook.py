import json


def loadBook():
    books = []
    try:
        with open('books.json', 'r') as fp:
            books = json.load(fp)
    except Exception as e:
        books = []
    return books

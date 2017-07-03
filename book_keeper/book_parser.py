import json
import os
from models import Book, Highlight

def create_book_models_from(directory_name):
    books = []
    files = os.listdir(directory_name)
    if len(files) > 0:
        for file_name in files:
            if file_name.endswith('.json'):
                path = os.path.join(directory_name, file_name)
                books.append(load_book(path))

    for books_json in books:
        parse_book(books_json)

def load_book(file_name):
    return json.load(open(file_name))

def parse_book(book):
    book_model = Book.create_from_kindle_json(book)
    book_model.save()
    book_model.add_categories_from_json(book)


    for highlight in book.get('highlights'):
        highlight_model = Highlight.create_from_kindle_json_and_book(highlight, book_model)
        highlight_model.save()








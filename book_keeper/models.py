from django.db import models

CATEGORY_CHOICES =

class Book(models.Model):
    asin = models.TextField()
    title = models.TextField()
    authors = models.TextField()
    categories = models.TextField('Category', blank=True)
    book_length = models.IntegerField(null=True)

    @classmethod
    def create_from_kindle_json(cls, json):
        book = cls()
        book.asin= json.get('asin', '')
        book.title = json.get('title', '')
        book.authors = json.get('authors', '')
        book.categories = []

        return book

    def add_categories_from_json(self, json):
       categories = json.get('categories')


class Highlight(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    text = models.TextField()
    book_location = models.IntegerField()

    @classmethod
    def create_from_kindle_json_and_book(cls, json, book):
        highlight = cls()
        highlight.book = book
        highlight.text = json.get('text')
        highlight.book_location = json.get('location', {}).get('value')

        return highlight





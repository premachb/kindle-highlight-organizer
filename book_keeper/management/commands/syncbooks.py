import os
from django.core.management.base import BaseCommand, CommandError
from book_keeper.book_parser import create_book_models_from

class Command(BaseCommand):
    help = 'Loads books and highlights from highlights directory'

    def handle(self, *args, **options):
        project_root = os.path.abspath(os.path.dirname(__name__))
        highlights_path = os.path.join(project_root, 'book_keeper/highlights')
        create_book_models_from(highlights_path)

from django.core.management.base import BaseCommand, CommandError
from book_keeper.models import Category

class Command(BaseCommand):
    help = 'Adds base categories to DB'

    def handle(self, *args, **options):
        category_names = ["Health", "Wealth", "Love", "Happiness"]
        for category_name in category_names:
            c = Category()
            c.name = category_name
            c.save()



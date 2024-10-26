import random

from django.core.management.base import BaseCommand
from faker import Faker
from books.models import Book


class Command(BaseCommand):
    help = 'Generate random book data for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=100,
            help='Number of books to create (default: 100)'
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']

        books = []
        for _ in range(count):
            book = Book(
                title=fake.sentence(nb_words=5),
                author=fake.name(),
                published_date=fake.date_between(start_date='-30y', end_date='today'),
                isbn=fake.isbn13(),
                pages=random.randint(50, 1000),
                cover=fake.image_url(),
                language=random.choice(['English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese']),
            )
            books.append(book)

        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} books.'))

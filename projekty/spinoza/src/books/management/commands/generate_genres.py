from django.core.management.base import BaseCommand
from books.fabrics import bulk_create_genres



class Command(BaseCommand):
    help = "Generate books"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)

    def handle(self, *args, **options):
        print("Generating genres...")

        n = options["n"]
        bulk_create_genres(n)

        print(f"Generated {n} genres")

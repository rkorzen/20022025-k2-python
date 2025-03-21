from django.core.management.base import BaseCommand
from books.fabrics import bulk_create_authors



class Command(BaseCommand):
    help = "Generate books"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)

    def handle(self, *args, **options):
        print("Generating authors...")

        n = options["n"]
        bulk_create_authors(n)

        print(f"Generated {n} authors")

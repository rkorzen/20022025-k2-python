from .models import Book, Author, Borrowing
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

def library_stats(request):
    return {
        "total_books": Book.objects.count(),
        "total_authors": Author.objects.count(),
        "total_borrowings": Borrowing.objects.count(),
        "books_borrowed": Borrowing.objects.filter(return_date__isnull=True).count(),
        "latests_books": Book.objects.order_by("-id")[:5],
        "books_borrowed_last_month": Borrowing.objects.filter(return_date__isnull=True, borrowing_date__gte=timezone.now() - timedelta(days=30)).count(),
        "popular_authors": [str(author) for author in Author.objects.annotate(book_count=Count("books")).order_by("-book_count")[:3]],
    }
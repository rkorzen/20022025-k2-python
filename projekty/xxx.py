
# context_processors.py
from .models import Book, Author, Borrowing
from django.db.models import Count
from django.utils import timezone

def library_stats(request):
    """
    Dodaje statystyki biblioteki do kontekstu każdego szablonu
    """
    return {
        'total_books': Book.objects.count(),
        'total_authors': Author.objects.count(),
        'books_borrowed': Borrowing.objects.filter(return_date__isnull=True).count(),
        'latest_books': Book.objects.all().order_by('-id')[:5],  # 5 ostatnio dodanych książek
        'popular_authors': Author.objects.annotate(
            book_count=Count('book')
        ).order_by('-book_count')[:3],  # 3 autorów z największą liczbą książek
    } 

# base.html
"""

  <div class="row">
        <div class="col-md-9">
            {% block content %}
            {% endblock %}
        </div>
        <div class="col-md-3">
            <div class="card mb-3">
                <div class="card-header">
                    <h5>Statystyki biblioteki</h5>
                </div>
                <div class="card-body">
                    <p>Liczba książek: {{ total_books }}</p>
                    <p>Liczba autorów: {{ total_authors }}</p>
                    <p>Aktualnie wypożyczone: {{ books_borrowed }}</p>
                </div>
            </div>

            <div class="card mb-3">
                <div class="card-header">
                    <h5>Ostatnio dodane książki</h5>
                </div>
                <div class="card-body">
                    <ul class="list-unstyled">
                    {% for book in latest_books %}
                        <li><a href="{% url 'book_details' book.id %}">{{ book.title }}</a></li>
                    {% endfor %}
                    </ul>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <h5>Najpopularniejsi autorzy</h5>
                </div>
                <div class="card-body">
                    <ul class="list-unstyled">
                    {% for author in popular_authors %}
                        <li>{{ author.name }} ({{ author.book_count }} książek)</li>
                    {% endfor %}
                    </ul>
                </div>
            </div>
        </div>
    </div>

"""
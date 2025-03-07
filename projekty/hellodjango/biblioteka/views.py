from django.shortcuts import render
from .services import Library, JsonAdapter
# Create your views here.
from .models import Book

def books_list(request):

    # db_adapter = JsonAdapter("dane/books.json")
    # library = Library(db_adapter)
    #
    # if request.GET.get("q"):
    #     books = library.search(request.GET.get("q"))
    # else:
    #     books = library.get_all_books()
    #


    if request.GET.get("q"):
        books = Book.objects.filter(title__icontains=request.GET["q"])
    else:
        books = Book.objects.all()

    context = {"books": books}

    return render(request, 'biblioteka/books_list.html', context=context)


def book_details(request, id):

    # db_adapter = JsonAdapter("dane/books.json")
    # library = Library(db_adapter)
    #
    # context = {"book": library.get_book_by_id(id)}

    context = {"book": Book.objects.get(id=id)}

    return render(request, 'biblioteka/book_details.html', context=context)
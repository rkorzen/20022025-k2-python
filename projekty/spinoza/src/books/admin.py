from django.contrib import admin
from .models import Author, Book, Genre, Borrowing
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    pass
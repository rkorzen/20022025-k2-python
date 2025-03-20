from django.contrib import admin
from .models import Author, Book, Genre, Borrowing
# Register your models here.

class BookInline(admin.TabularInline):
    model = Book
    fields = ["title", "genre"]
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "is_available")

    def is_available(self, obj):
        return obj.is_available

    is_available.boolean = True
    is_available.short_description = "Czy dostępna"


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    pass
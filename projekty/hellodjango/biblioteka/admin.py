from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "available"]
    readonly_fields = ["added_on", "updated_on"]
    list_filter = ["available"]
    search_fields = ["title", "author"]

admin.site.register(Book, BookAdmin)


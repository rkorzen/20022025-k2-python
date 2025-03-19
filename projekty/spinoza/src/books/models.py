from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(help_text="Enter a brief description of the book", blank=True)
    isbn = models.CharField(max_length=13, help_text="13 Character ISBN number", blank=True, null=True)
 
    def __str__(self):
        return f"{self.title} ({self.author})"
    
    @property
    def is_available(self):
        # sprawdź czy istnieje wypożyczenie, które nie zostało zwrócone
        return not self.borrowing_set.last().return_date is None if self.borrowing_set.last() else True

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    user = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.book}"


# book.review_set.all()


class Borrowing(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} ({self.borrowing_date} - {self.return_date})"
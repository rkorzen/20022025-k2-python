from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Book(models.Model):

    GENRES = (
        ('fiction', 'Fiction'),
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('animation', 'Animation'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('fantasy', 'Fantasy'),
        ('horror', 'Horror'),
        ('music', 'Music'),
    )

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField(validators=[MaxValueValidator(2025)])
    isbn = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True, choices=GENRES)
    available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    last_borrowed_on = models.DateTimeField(blank=True, null=True)
    last_return_on = models.DateTimeField(blank=True, null=True)




    def __str__(self):
        return f"({self.id}) {self.title}"
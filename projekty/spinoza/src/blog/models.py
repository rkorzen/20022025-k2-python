from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Post(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return self.title



class Comment(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("rejected", "Rejected"),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="draft")

# Dodaj model Comment - który jest powiązany z modelem Post i Author.
# Komentarz ma mieć pola:
# - content - tekst komentarza
# - created_at - data dodania komentarza
# - updated_at - data ostatniej modyfikacji komentarza
# - post - powiązanie z modelem Post
# - author - powiązanie z modelem User
# - status - status komentarza (na_czekaniu, opublikowany, odrzucony)
#            
#  Dodaj formularz do dodawania komentarza.
#  Komentarz może być dodawany tylko przez zalogowanego użytkownika i widoku post_detail.html.
#  Wyslanie formularza powinno wysylac request metodą POST do widoku /blog/post/<pk>/add-comment/
#  po utworzeniu komentarza wracamy na widok szzegolow danego posta i komentarz powinien byc widoczny pod postem.
#  Dodaj w Paneu admina mozliwosc moderowania komentarzy - Inline do postu.
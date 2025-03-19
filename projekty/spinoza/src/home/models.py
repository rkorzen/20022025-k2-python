from django.db import models

# Create your models here.

class Contact(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("closed", "Closed"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    asigned_to = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    comment = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="new")


    def __str__(self):
        return self.name
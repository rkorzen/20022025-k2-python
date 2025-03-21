from django.db import models
from pygments.styles import get_all_styles
from pygments.lexers import get_all_lexers
# Create your models here.

LANGUAGE_CHOICES = [(item[1][0], item[0]) for item in get_all_lexers() if item[1]]
STYLE_CHOICES = [(item, item) for item in get_all_styles()]

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)

    class Meta:
        ordering = ["created"]
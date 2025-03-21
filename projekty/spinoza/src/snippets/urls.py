from django.urls import path
from .views import snippet_list

urlpatterns = [
    path("snippets/", snippet_list)
]
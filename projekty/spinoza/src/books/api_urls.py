from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .api_views import genre_list, author_list, genre_detail, author_detail

urlpatterns = [
    path("genres/", genre_list),
    path("genres/<int:pk>/", genre_detail),
    path("authors/", author_list),
    path("authors/<int:pk>/", author_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)
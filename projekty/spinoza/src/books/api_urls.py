from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .api_views import GenreList, GenreDetail, AuthorList, AuthorDetail

app_name="apibooks"
urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("authors/", AuthorList.as_view(), name="author_list"),
    path("authors/<int:pk>/", AuthorDetail.as_view(), name="author_detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
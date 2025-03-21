from rest_framework import generics
from .models import Genre, Author
from .serializers import GenreSerializer, AuthorSerializer


class GenreList(generics.ListCreateAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

 
class AuthorList(generics.ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

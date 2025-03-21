
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Genre, Author
from .serializers import GenreSerializer, AuthorSerializer

@api_view(["GET", "POST"])
def genre_list(request, format=None):

    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    
@api_view(["GET", "PUT", "DELETE"])
def genre_detail(request, pk, format=None):

    genre = Genre.objects.get(pk=pk)

    if request.method == "GET":
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == "PUT":
        
        serializer = GenreSerializer(instance=genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        genre.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def author_list(request, format=None):

    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def author_detail(request, pk,  format=None):

    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == "PUT":
        
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == "PATCH":
        data = dict(request.data)
        
        data["first_name"] = data.get("first_name", author.first_name)
        data["last_name"] = data.get("last_name", author.last_name)
        data["date_of_birth"] = data.get("date_of_birth", author.date_of_birth)
        data["date_of_death"] = data.get("date_of_death", author.date_of_death)

        serializer = AuthorSerializer(instance=author, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        author.delete()
        return Response(status=204)

    else:
        return Response(status=405)
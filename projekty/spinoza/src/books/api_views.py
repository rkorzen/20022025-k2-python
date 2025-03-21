from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Genre, Author
from .serializers import GenreSerializer, AuthorSerializer

@csrf_exempt
def genre_list(request):

    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    
@csrf_exempt
def genre_detail(request, pk):

    genre = Genre.objects.get(pk=pk)

    if request.method == "GET":
        serializer = GenreSerializer(genre)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = GenreSerializer(instance=genre, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        genre.delete()
        return HttpResponse(status=204)


@csrf_exempt
def author_list(request):

    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def author_detail(request, pk):

    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(instance=author, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "PATCH":
        data = JSONParser().parse(request)
        
        data["first_name"] = data.get("first_name", author.first_name)
        data["last_name"] = data.get("last_name", author.last_name)
        data["date_of_birth"] = data.get("date_of_birth", author.date_of_birth)
        data["date_of_death"] = data.get("date_of_death", author.date_of_death)

        serializer = AuthorSerializer(instance=author, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        author.delete()
        return HttpResponse(status=204)

    else:
        return HttpResponse(status=405)
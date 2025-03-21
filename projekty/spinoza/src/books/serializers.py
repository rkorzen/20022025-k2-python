from rest_framework.serializers import ModelSerializer, SlugField
from books.models import Author, Genre

class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ["first_name", "last_name", "date_of_birth", "date_of_death", "bio"]

class GenreSerializer(ModelSerializer):
    slug = SlugField(read_only=True)

    class Meta:
        model = Genre
        fields = ["name", "slug", "description"]

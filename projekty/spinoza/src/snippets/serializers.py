from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]



class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")
    class Meta:
        model = Snippet
        fields = ["url", "id", "highlight", "title", "code", "linenos", "language", "style", "owner"]
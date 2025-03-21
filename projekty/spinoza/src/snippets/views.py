from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer

from .permissions import IsOwnerOrReadOnly

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "snippets": reverse("snippet-list", request=request, format=format),
    })


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)



class SnippetList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, 
    ]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# class UserList(generics.ListAPIView):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

    
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



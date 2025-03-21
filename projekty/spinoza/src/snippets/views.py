
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(ListModelMixin, CreateModelMixin, generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class SnippetDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    
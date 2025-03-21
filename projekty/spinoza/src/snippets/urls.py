from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetList, SnippetDetail, api_root, SnippetHighlight

from .views import UserViewSet

user_list = UserViewSet.as_view({
    "get": "list"
})

user_details = UserViewSet.as_view({
    "get": "retrieve"
})


urlpatterns = [
    path("", api_root),
    path("snippets/", SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>", SnippetDetail.as_view(), name="snippet-detail"),
    path("snippets/<int:pk>/highlight/", SnippetHighlight.as_view(), name="snippet-highlight"),

    path("users/", user_list, name="user-list"),
    path("users/<int:pk>", user_details, name="user-detail"),

    

]

urlpatterns = format_suffix_patterns(urlpatterns)
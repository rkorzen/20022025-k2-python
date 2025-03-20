from django.urls import path
from .views import PostListView, post_list 
from .views import post_detail, PostDetailView
from .views import post_add, PostCreateView

urlpatterns = [
    path("posts/f/", post_list, name="post_list_f"),
    path("posts/c/", PostListView.as_view(), name="post_list_c"),


    path("posts/f/<int:id>", post_detail, name="post_detail_f"),
    path("posts/c/<int:pk>", PostDetailView.as_view(), name="post_detail_c"),

    path("posts/f/add/", post_add, name="post_add_f"),
    path("posts/c/add/", PostCreateView.as_view(), name="post_add_c"),

]
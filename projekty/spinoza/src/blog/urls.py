from django.urls import path
from .views import PostListView, post_list 
from .views import post_detail, PostDetailView
from .views import post_add, PostCreateView
from .views import post_edit, PostUpdateView
from .views import post_delete, PostDeleteView

urlpatterns = [

    # READ or CREATE
    path("posts/f/", post_list, name="post_list_f"),
    path("posts/c/", PostListView.as_view(), name="post_list_c"),

    # READ
    path("posts/f/<int:pk>", post_detail, name="post_detail_f"),
    path("posts/c/<int:pk>", PostDetailView.as_view(), name="post_detail_c"),

    # CREATE
    path("posts/f/add/", post_add, name="post_add_f"),
    path("posts/c/add/", PostCreateView.as_view(), name="post_add_c"),

    # UPDATE
    path("posts/f/<int:pk>/edit/", post_edit, name="post_edit_f"),
    path("posts/c/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit_c"),

    # DELETE
    path("posts/f/<int:pk>/delete/", post_delete, name="post_delete_f"),
    path("posts/c/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete_c"),

    # add comment
    path("posts/f/<int:pk>/add-comment/", post_add_comment, name="add_comment"),
    # path("posts/c/<int:pk>/add-comment/", post_add_comment, name="post_add_comment"),
    # path("posts/c/<int:pk>/add-comment/", PostAddCommentView.as_view(), name="post_add_comment_c"),

]
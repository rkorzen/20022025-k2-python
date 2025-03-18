from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.posts_list, name='index'),
    path('posts/<int:id>', views.post_details, name='details'),
]
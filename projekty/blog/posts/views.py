from django.shortcuts import render

from posts.models import Post


# Create your views here.

def posts_list(request):
    posts = Post.objects.filter(is_published=True)
    context = {'posts': posts}
    return render(request, "posts/post_list.html", context)

def post_details(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, "posts/post_details.html", context)
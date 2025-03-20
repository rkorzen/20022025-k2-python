from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your views here.

def post_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.slug = slugify(instance.title)
            instance.save()
            return redirect("post_list_f")
    
    form = PostForm()
    posts = Post.objects.filter(status="published")
    return render(request, "blog/post_list.html", {"object_list": posts, "current_page": "posts_f", "form": form})


class PostListView(ListView):
    model = Post
    # context_object_name = "posts"  # default: object_list

    def get_queryset(self):
        return Post.objects.filter(status="published")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "posts_c"
        context["form"] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.slug = slugify(instance.title)
            instance.save()
            return redirect("post_list_c")
        return super().post(request, *args, **kwargs)



def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status="published")
    return render(request, "blog/post_detail.html", {"object": post, "current_page": "posts_f"})


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "posts_c"
        return context
    
    def get_queryset(self):
        return Post.objects.filter(status="published")


def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.slug = slugify(instance.title)
            instance.save()
            return redirect("post_list_f")
    
    form = PostForm()

    return render(request, "blog/post_form.html", {"current_page": "posts_f", "form": form})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("post_list_c")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
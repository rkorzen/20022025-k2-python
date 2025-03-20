from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import CommentForm
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


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status="published")
    comment_form = CommentForm()
    return render(request, "blog/post_detail.html", {"object": post, "current_page": "posts_f", "comment_form": comment_form})


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "posts_c"
        context["comment_form"] = CommentForm()
        return context
    
    def get_queryset(self):
        return Post.objects.filter(status="published")


@login_required
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


class PostCreateView(LoginRequiredMixin, CreateView):
    
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("post_list_c")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail_c", pk=pk)
    
    if post.user != request.user:
        messages.error(request, "Nie jesteś autorem tego posta")
        return redirect("post_detail_f", pk=pk)
    
    form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form, "current_page": "posts_f"})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("post_list_c")


    def test_func(self):
        post = self.get_object()
        if post.user == self.request.user:
            return True
        messages.error(self.request, "Nie jesteś autorem tego posta")
        return redirect("post_detail_f", pk=post.pk)
    

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:
        messages.error(request, "Nie jesteś autorem tego posta")
        return redirect("post_detail_f", pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post_list_c")
    return render(request, "blog/post_confirm_delete.html", {"object": post})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list_c")

    def test_func(self):
        post = self.get_object()
        return post.user == self.request.user
    

@login_required
def post_add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.author = request.user
            instance.save()

    return redirect("post_detail_f", pk=pk)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy("post_detail_c", kwargs={"pk": self.kwargs["pk"]})
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)
    
    
    
    
    
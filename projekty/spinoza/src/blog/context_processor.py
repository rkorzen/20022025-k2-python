from .models import Post
from django.db.models import Count
def blog_stats(request):
    return {
        "total_posts": Post.objects.count(),
        "posts_with_most_comments": Post.objects.annotate(total_comments=Count("comment")).order_by("-total_comments").values_list("title", flat=True)[:3],
    }

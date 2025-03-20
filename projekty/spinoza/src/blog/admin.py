from django.contrib import admin
from django.db.models.functions import Length
from django.utils import timezone
from datetime import timedelta
# Register your models here.

from .models import Post, Comment


@admin.action(description="Mark selected comments as published")
def mark_as_published(modeladmin, request, queryset):
    queryset.update(status="published")


@admin.action(description="Mark selected comments as draft")
def mark_as_draft(modeladmin, request, queryset):
    queryset.update(status="draft")


@admin.action(description="Mark selected comments as rejected")
def mark_as_rejected(modeladmin, request, queryset):
    queryset.update(status="rejected")



class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at", "body_length", "recently_published")
    readonly_fields = ("created_at", "updated_at", "body_length", "recently_published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentInline]
    actions = [mark_as_draft, mark_as_published]

    def body_length(self, obj):
        return obj._body_length


    def recently_published(self, obj):
        return obj.status == "published" and obj.created_at > timezone.now() - timedelta(days=10)

    recently_published.boolean = True

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_body_length=Length("body"))
        return queryset

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "author", "post", "created_at", "status")
    actions = [mark_as_published, mark_as_draft, mark_as_rejected]
    list_filter = ("status", "post")
    search_fields = ["content"]

admin.site.register(Comment, CommentAdmin)



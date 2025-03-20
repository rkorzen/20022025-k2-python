from django.contrib import admin

# Register your models here.

from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)


@admin.action(description="Mark selected comments as published")
def mark_as_approved(modeladmin, request, queryset):
    queryset.update(status="published")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "author", "post", "created_at", "status")
    actions = [mark_as_approved]    

admin.site.register(Comment, CommentAdmin)



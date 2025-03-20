from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

from django.contrib import admin
from .models import Tag
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Tag, TagAdmin)

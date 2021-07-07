from pages.models import Blog
from django.contrib import admin

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image', 'created_at')
    list_filter = ('title', 'author__username')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, BlogAdmin)

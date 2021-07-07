from pages.models import Bio, Blog, Category, Gallery
from django.contrib import admin

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image', 'created_at')
    list_filter = ('title', 'author__username')
    prepopulated_fields = {"slug": ("title",)}


class BioAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image', 'created_at')
    list_filter = ('title', 'author__username')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'author', 'created_at')
    list_filter = ('categories', 'author')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'created_at')
    list_filter = ('cat_name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Bio, BioAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category, CategoryAdmin)

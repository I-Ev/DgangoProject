from django.contrib import admin

from blog.models import BlogEntry



@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'body', 'preview', 'is_published')

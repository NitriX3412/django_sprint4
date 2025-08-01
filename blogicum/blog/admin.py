from django.contrib import admin

from .models import Category, Location, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'category',
        'location',
        'created_at',
        'is_published'
    )

    list_editable = (
        'is_published',
        'category'
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title'

class LocationAdmin(admin.ModelAdmin):
    list_display = 'name'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text_short')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Comment)
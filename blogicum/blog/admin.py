from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'slug')
        }),
        ('Настройки публикации', {
            'fields': ('is_published',)
        }),
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)
    list_editable = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'pub_date')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'text', 'author')
        }),
        ('Настройки публикации', {
            'fields': ('category', 'location', 'is_published', 'pub_date')
        }),
    )

    readonly_fields = ('created_at',)

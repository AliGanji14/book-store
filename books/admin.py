from django.contrib import admin

from .models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'author', 'price', 'price',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'datetime_created', 'recommend', 'is_active')

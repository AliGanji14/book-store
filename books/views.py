from django.shortcuts import render
from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list_view.html'

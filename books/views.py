from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    context_object_name = 'books'
    template_name = 'books/book_list.html'


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comment = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'book_comment': book_comment})


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ('title', 'author', 'description', 'price', 'cover')


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ('title', 'author', 'description', 'price', 'cover')
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

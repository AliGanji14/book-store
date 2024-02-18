from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from books.models import Book
from books.forms import CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    context_object_name = 'books'
    template_name = 'books/book_list.html'


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comment = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'book_comment': book_comment,
        'comment_form': comment_form,
    })


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

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import CommentForm, BookForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    context_object_name = 'books'
    template_name = 'books/book_list.html'


@login_required(login_url='/accounts/login/')
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


@login_required
def book_create_view(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        new_book = book_form.save(commit=False)
        new_book.user = request.user
        new_book.save()
        return redirect(new_book)
    else:
        book_form = BookForm()
    return render(request, 'books/book_create.html', {"form": book_form})


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ('title', 'author', 'description', 'price', 'cover')
    template_name = 'books/book_update.html'


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

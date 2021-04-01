from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book
from author.models import Author
from order.models import Order
from django.contrib.auth import get_user
from datetime import datetime
from authentication.decorators import is_admin


def list_of_books(request):
    books = list(Book.get_all())
    # authors = [list(book.authors.all()) for book in books]
    # zipped = zip(books, authors)
    ordered_books = [order.book for order in Order.get_all() if order.user == get_user(request) and not order.end_at]
    print(ordered_books)
    return render(request, 'list_of_books.html', {'books':books, 'ordered_books':ordered_books})


@login_required(login_url='login')
@is_admin
def new_book(request):
    data = {}
    all_authors = Author.get_all()
    data['all_authors'] = all_authors
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        count = int(request.POST['count'])
        authors = dict(request.POST)['authors']
        book = Book.create(name, description, count, authors)
        if book:
            data['res'] = 'Book has been added!'
            return render(request, 'new_book.html', data)
        else:
            data['res'] = 'Error!'
            return render(request, 'new_book.html', data)
        
    return render(request, 'new_book.html', data)


@login_required(login_url='login')
@is_admin
def edit_book(request, pk):
    book = Book.get_by_id(pk)
    all_authors = Author.get_all()
    if request.method == 'POST':
        if 'add' in request.POST:
            book.add_authors(dict(request.POST)['all_authors'])
        elif 'remove' in request.POST:
            book.remove_authors(dict(request.POST)['authors'])
        else:
            name = request.POST['name']
            description = request.POST['description']
            count = request.POST['count']
            book.update(name=name, description=description, count=count)
    return render(request, 'edit_book.html', {'book':book, 'authors':book.authors.all(), 'all_authors':all_authors})


@login_required(login_url='login')
@is_admin
def delete_book(request, pk):
    Book.delete_by_id(pk)
    return redirect('list of books')
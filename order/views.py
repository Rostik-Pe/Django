from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from authentication.decorators import is_admin
from .models import Order
from book.models import Book
import datetime

@login_required(login_url='login')
def list_of_orders(request):
    data ={}
    data['orders'] = Order.get_all()
    return render(request, 'list_of_orders.html', data)


@login_required(login_url='login')
def new_order(request, pk):
    user = get_user(request)
    book = Book.get_by_id(pk)
    current_date = datetime.datetime.today()
    future_date = current_date + datetime.timedelta(days=15)
    Order.create(user=user, book=book, plated_end_at=future_date)
    book.update(count=book.count-1)
    data = {}
    data['book'] = book
    authors = []
    for i in book.authors.all():
        authors.append(i)
    data['authors'] = authors
    return render(request, 'new_order.html', data)

@login_required(login_url='login')
def return_book(request, pk):
    order = Order.get_by_id(pk)
    order.update(end_at=datetime.datetime.today())
    book = order.book
    book.update(count=book.count + 1)
    return redirect('list of orders')

@login_required(login_url='login')
@is_admin
def delete_order(request, pk):
    order = Order.get_by_id(pk)
    if not order.end_at:
        order.book.update(count= order.book.count + 1)
    Order.delete_by_id(pk)
    return redirect('list of orders')

@login_required(login_url='login')
@is_admin
def not_returned_books(request):
    not_returned = Order.get_not_returned_books()
    return render(request, 'not_returned_books.html', {'orders':not_returned})
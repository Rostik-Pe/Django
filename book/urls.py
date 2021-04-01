from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_books, name='list of books'),
    path('new_book/', views.new_book, name='new book'),
    path('edit/<int:pk>/', views.edit_book, name='edit book'),
    path('delete/<int:pk>', views.delete_book, name='delete book'), 
]
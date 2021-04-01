from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_orders, name='list of orders'),
    path('order/<int:pk>/', views.new_order, name='new_order'),
    path('delete/<int:pk>', views.delete_order, name='delete order'),
    path('return/<int:pk>', views.return_book, name='return book'),
    path('not_returned_books', views.not_returned_books, name='not returned books'),
]
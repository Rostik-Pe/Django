from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_authors, name='list of authors'),
    path('new_author/', views.new_author, name='new author'),
    path('edit_author/<int:pk>', views.edit_author, name='edit author'),
    path('delete_author/<int:pk>', views.delete_author, name='delete author'),
]
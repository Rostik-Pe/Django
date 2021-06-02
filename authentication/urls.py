from django.urls import path
from . import views
from . import forms


urlpatterns = [
    path('', views.index, name='homepage'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('users/', views.users, name='users'),
    path('edit_user/<int:pk>', views.edit_user, name='edit user'),
    path('delete_user/<int:pk>', views.delete_user, name= 'delete user'),
    path('logged_out/', views.logout_user, name='logged_out'),
    path('access_denied/', views.access_denied, name='access denied'),
    # path("", views.register_view, name="register view")
]
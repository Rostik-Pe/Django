from django.shortcuts import render, redirect
from .models import CustomUser
from book.models import Book
from author.models import Author
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .decorators import is_admin
from django.http import HttpResponse
from .forms import RegisterForm

def index(request):
    all_books = len(Book.get_all())
    all_authors = len(Author.get_all())
    all_copies = 0
    for book in Book.get_all():
        all_copies += book.count
    return render(request, 'index.html', {'all_books':all_books, 'all_authors':all_authors, 'all_copies':all_copies})

# def register_user(request):
#     message = ''
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         middle_name = request.POST['middle_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         repeat_password = request.POST['repeat_password']
#         if password == repeat_password:
#             user = CustomUser.create(email=email,
#                             password=password,
#                             first_name=first_name,
#                             middle_name=first_name,
#                             last_name=last_name)
#             if user:
#                 message = "User successfully registered!"
#             else:
#                 message = "User already exists!"
#         else:
#             message = "Passwords don't match!"
#     return render(request, 'register.html', {'message':message})

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.get_by_email(email)
        if user and user.check_password(password):
            if user.is_active:
                login(request, user)
                return redirect('list of books')
            else:
                message = 'User is not active!'
                return render(request, 'login.html', {'message':message})
        else:
            message = 'Invalid email or password!'
            return render(request, 'login.html', {'message':message})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return render(request, 'logout.html')

@login_required(login_url='login')
@is_admin
def users(request):
    return render(request, 'users.html', {'users':CustomUser.get_all()})

@login_required(login_url='login')
@is_admin
def edit_user(request, pk):
    user = CustomUser.get_by_id(pk)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        role = request.POST['role']
        is_active = True if 'is_active' in request.POST.keys() else False
        user.update(first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    role=role,
                    is_active=is_active)
        return redirect('users')
    return render(request, 'edit_user.html', {'current_user':user})

@is_admin
def delete_user(request, pk):
    user = CustomUser.delete_by_id(pk)
    return redirect('users')

def access_denied(request):
    return render(request, 'access_denied.html')



def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = RegisterForm()
    print(form)
    return render(request, "register.html", {"form": form})
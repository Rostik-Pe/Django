from django.shortcuts import render, redirect
from .models import CustomUser
from book.models import Book
from author.models import Author
from .forms import EditForm, LoginForm
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

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.get_by_email(email)
        if user and user.check_password(password):
            if user.is_active:
                login(request, user)
                return redirect('list of books')
            else:
                form = LoginForm(request.POST)
                message = 'User is not active!'
                return render(request, 'login.html', {'form':form, 'message':message})
        else:
            message = 'Invalid email or password!'
            return render(request, 'login.html', {'form':form, 'message':message})
    return render(request, 'login.html', {'form':form})

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
    form = EditForm(user.to_dict())
    if request.method == 'POST':
        is_active = True if 'is_active' in request.POST.keys() else False
        user.update(first_name=request.POST['first_name'],
                    middle_name=request.POST['middle_name'],
                    last_name=request.POST['last_name'],
                    role=request.POST['role'],
                    is_active=is_active)
        return redirect('users')
    return render(request, 'edit_user.html', {'form':form, 'current_user':user})

@is_admin
def delete_user(request, pk):
    user = CustomUser.delete_by_id(pk)
    return redirect('users')

def access_denied(request):
    return render(request, 'access_denied.html')


def register_user(request):
    form = RegisterForm()
    print(form)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
    return render(request, "register.html", {"form": form})
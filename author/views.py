from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.decorators import is_admin
from .forms import AuthorForm
from .models import Author

def list_of_authors(request):
    data = {}
    data['authors'] = Author.get_all()
    return render(request, 'list_of_authors.html', data)


@login_required(login_url='login')
@is_admin
def new_author(request):
    data = {}
    form = AuthorForm()
    data['form'] = form
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        name =request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        author = Author.create(name, surname, patronymic)
        if author:
            form = AuthorForm()
            data['form'] = form
            data['res'] = 'Author has been added!'
        else:
            form = AuthorForm(request.POST)
            data['form'] = form
            data['res'] = 'Error!'
    return render(request, 'new_author.html', data)

# @login_required(login_url='login')
# @is_admin
# def edit_author(request, pk):
#     author = Author.get_by_id(pk)
#     if request.method == 'POST':
#         name = request.POST['name']
#         surname = request.POST['surname']
#         patronymic = request.POST['patronymic']
#         author.update(name=name, surname=surname, patronymic=patronymic)
#     print(author)
#     return render(request, 'edit_author.html', {'author':author})


@login_required(login_url='login')
@is_admin
def delete_author(request, pk):
    Author.delete_by_id(pk)
    return redirect('list of authors')


@login_required(login_url='login')
@is_admin
def edit_author(request, pk):
    form = AuthorForm(request.POST)
    author = Author.get_by_id(pk)
    if request.method == 'POST':
        author.update(name=request.POST['name'],
                      surname=request.POST['surname'],
                      patronymic=request.POST['patronymic'])
    print(author)
    return render(request, 'edit_author.html', {'author': author,
                                                'form': form
                                                })
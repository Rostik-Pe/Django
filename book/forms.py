from django.forms import ModelForm, Form
from book.models import Book



class EditBookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'description', 'count']

class RemoveAuthors(ModelForm):

    class Meta:
        model = Book
        fields = ['authors']

class AddAuthors(Form):

    pass


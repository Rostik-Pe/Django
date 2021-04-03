from django import forms
from book.models import Book
from author.models import Author

class AuthorMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name} {obj.surname}' 

class NewBookForm(forms.ModelForm):

    all_authors = AuthorMultipleChoiceField(Author.get_all())

    class Meta:
        model = Book
        fields = ['name', 'description', 'count']
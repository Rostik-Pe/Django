from django import forms
from book.models import Book
from author.models import Author


class EditBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'description', 'count']


class RemoveAuthors(forms.Form):

    authors = None

    def __init__(self, pk):

        super(RemoveAuthors, self).__init__()

        self.fields['authors'] = forms.ModelMultipleChoiceField(Book.get_by_id(pk).authors)


class AddAuthors(forms.Form):

    all_authors = forms.ModelMultipleChoiceField(Author.get_all())


class NewBookForm(forms.ModelForm):

    all_authors = forms.ModelMultipleChoiceField(Author.get_all())

    class Meta:
        model = Book
        fields = ['name', 'description', 'count']


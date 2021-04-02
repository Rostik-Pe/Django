from django import forms
from .models import CustomUser

class EditForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name', 'role', 'is_active')
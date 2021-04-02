from django.forms import ModelForm
from authentication.models import CustomUser
from django import forms


class RegisterForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password']


# class RegisterForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     middle_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField()
#     repeat_password = forms.CharField()

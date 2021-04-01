from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import get_user

def is_admin(func):
    def wrapper(request, *args, **kwargs):
        user = get_user(request)
        if user.role:
           return func(request, *args, **kwargs)
        return redirect('access denied')
    return wrapper
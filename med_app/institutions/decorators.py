from django.http import HttpResponse
from django.shortcuts import redirect

def user_unauthenticated(view_access):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_access(request, *args, **kwargs)
            
    return wrapper_func
# from django.shortcuts import render

# def login(request):
#     return render(request, 'account/login.html')

# def password(request):
#     return render(request, 'account/password.html')

# def register(request):
#     return render(request, 'account/register.html')

from django.shortcuts import render, redirect
from .models import User

def login(request):
    return render(request, 'account/login.html')

def password(request):
    return render(request, 'account/password.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return redirect('account:login')
        else:
            # Handle password mismatch error
            return render(request, 'account/register.html', {'error': 'Passwords do not match'})

    return render(request, 'account/register.html')

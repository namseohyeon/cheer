from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
from .forms import signupForm
# Create your views here.

def login(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            return redirect('main')
        return redirect('signup')
    else:
        form = signupForm()
    return render(request, 'signup.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('main')

def mypage(request):
    return render(request, 'mypage.html')
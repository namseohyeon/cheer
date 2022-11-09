from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import signupForm
# Create your views here.

def login(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request=request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        return redirect('mypage')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            return redirect('mypage')
        return redirect('signup')
    else:
        form = signupForm()
    return render(request, 'signup.html',{'form':form})


def mypage(request):
    return render(request, 'mypage.html')
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.user.is_authenticated:
        return redirect('counter:home')

    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('counter:home')
    elif request.method == "GET":
        login_form = AuthenticationForm()
        return render(request, 'auth_cal:login.html', {'login_form': login_form})
    
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('counter:home')
    
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        print(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            return redirect('auth_cal:login')
    else:
        signup_form = UserCreationForm()
    
    return render(request, 'auth_cal:signup.html', {'signup_form': signup_form})

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('auth_cal:login')
    logout(request)
    return redirect('auth_cal:login')
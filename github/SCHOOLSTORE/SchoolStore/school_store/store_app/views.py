from django.contrib import auth,messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store_app:formpage')

        messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('store_app:register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('store_app:login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('store_app:register')

    return render(request, "register.html")


def user_profile(request):
    confirmation_message = None

    if request.method == 'POST':

        confirmation_message = 'Order Confirmed'
        print("Confirmation Message:", confirmation_message)
        return render(request, 'formpage.html', {'confirmation_message': confirmation_message})

    return render(request, 'formpage.html', {'confirmation_message': confirmation_message})

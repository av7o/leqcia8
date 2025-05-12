from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth import authenticate  # Import the authenticate function
from django.contrib import messages  # Import the messages framework

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save(commit=False)  # Create the user object but don't save yet
            user.username = form.cleaned_data['username']  # Get the username
            user.set_password(form.cleaned_data['password1'])  # Hash the password
            user.save()  # Save the user to the database
            messages.success(request, 'Registration successful! You can now log in.')  # Add success message
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')  # Add success message
                return redirect('dashboard')  # Redirect to the dashboard page after login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def custom_logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')  # Add info message
    return redirect('login')  # Redirect to the login page

def home_view(request):
    return render(request, 'users/home.html')

@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')

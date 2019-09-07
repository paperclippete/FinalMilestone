from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from membership.models import Membership
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.


@login_required    
def logout(request):
    """Logout user and end session"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))


def login(request):
    """Return a Login Page and log the user in"""
    login_form = UserLoginForm(request.POST or None)
    context = {
        'login_form': login_form,
    }
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        if login_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])
            if user: 
                auth.login(user=user, request=request)
                messages.success(request, f"Welcome {user.first_name}, you have successfully logged in!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Your username or password is incorrect!")
                  
    else:
        return render(request, 'login.html', context)
    
    return render(request, 'login.html', context)            
                

def register(request):
    """Return a registration form and create a new authorised user"""
    registration_form = UserRegistrationForm(request.POST or None)
    context = {
        'registration_form': registration_form
    }
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        if registration_form.is_valid():
            # Ensure username saves as lowercase to the db
            registration_form.save()
            user = auth.authenticate(username=request.post['username'],
                                     password=request.post['password1'])
            membership = Membership(user=user)
            membership.save()
            if user:
                auth.login(user=user, request=request)
                messages.success(request, f"{user.first_name}, you have successfully registered!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    
    return render(request, 'register.html', context)
    
@login_required     
def user_profile(request):
    """The user's profile page"""
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
        context = {
            'profile': user
        }
        return render(request, 'profile.html', context)
    else:
        return redirect(reverse('login'))
    
    
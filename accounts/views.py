from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from membership.models import Membership
from events.models import Like, Participant, Event
from .forms import UserLoginForm, UserRegistrationForm, EditUserForm
from membership.forms import OrderMembershipForm
from django.conf import settings
import stripe
import datetime


@login_required    
def logout(request):
    """Logout user and end session"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))

def login(request):
    """Return a Login page for @login or unsuccessful modal login"""
    login_form = UserLoginForm(request.POST or None)
    return render(request, 'login.html', {'login_form': login_form}) 

def login_modal(request):
    """Return a Login Page and log the user in"""
    login_form = UserLoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    user = auth.authenticate(request.POST['username_or_email'],
                             password=request.POST['password'])
    if user: 
        auth.login(user=user, request=request)
        messages.success(request, f"Welcome {user.first_name}, you have successfully logged in!")
        return redirect(reverse('index'))
    else:
        messages.error(request, "Wrong username or password, try again!")
        return render(request, 'login.html')          
    

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
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
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
    user = get_object_or_404(User, pk=request.user.id)
    user_liked = Like.objects.filter(user=user).values('event')
    user_liked_events = Event.objects.filter(id__in=user_liked).order_by('event_date_begins')
    user_participant = Participant.objects.filter(user=user).values('event')
    user_participant_events = Event.objects.filter(id__in=user_participant).exclude(event_date_ends__lt=datetime.date.today()).order_by('event_date_begins')
    user_participated_events = Event.objects.filter(id__in=user_participant).exclude(event_date_ends__gt=datetime.date.today()).order_by('-event_date_begins')
    user_hosted_events = Event.objects.filter(event_host=user).exclude(event_date_ends__lt=datetime.date.today()).order_by('event_date_begins')
    user_past_hosted_events = Event.objects.filter(event_host=user).exclude(event_date_ends__gt=datetime.date.today()).order_by('-event_date_begins')
    membership = Membership.objects.get(user=user)
    edit_form = EditUserForm(instance=request.user)
    order_form = OrderMembershipForm(request.POST or None, instance=request.user)
    if request.method == "POST":
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "You have updated your details!")
    context = {
        'user': user,
        'membership': membership,
        'edit_form': edit_form,
        'order_form': order_form,
        'publishable': settings.STRIPE_PUBLISHABLE,
        'user_liked_events': user_liked_events,
        'user_participant_events': user_participant_events,
        'user_hosted_events': user_hosted_events,
        'user_participated_events': user_participated_events,
        'user_past_hosted_events': user_past_hosted_events
        
    }
    return render(request, 'profile.html', context)
    
    
    
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm, JoinEvent, LikeEvent
from django.urls import reverse, reverse_lazy
from .models import Event, Participant, Like
from membership.models import Membership
from django.contrib.auth.models import User
import datetime


# Create your views here.
@login_required
def post_event(request):
    """Renders Create Event Form"""
    event_form = CreateEventForm()
    user = request.user
    if request.method == "POST":
        event_form = CreateEventForm(request.POST, request.FILES)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.event_host = user
            event.save()
            membership = Membership.objects.get(user=user)
            membership.posts_remaining -= 1
            membership.save()
            current_places = event.max_participants
            full_address = event.address + ' ' + event.town + ' ' + event.post_code
            context = {
                'event': event,
                'current_places': current_places,
                'full_address': full_address,
                'event_host': event.event_host,
            }
            messages.success(request, f"You have posted {request.POST['title']}!")
            return render(request, 'view_one_event.html', context)

    context = {
        'event_form': event_form
    }

    return render(request, 'post_event.html', context)
    
@login_required
def edit_event(request, pk):
    """Allows Event Host to make changes to an upcoming event and re-publish a finished event"""
    event = get_object_or_404(Event, pk=pk)
    event_form = CreateEventForm(request.POST or None, instance=event)
    context = {
        'event_form': event_form
    }
    user = request.user
    if request.method == "POST" and event_form.is_valid():
        edit = event_form.save(commit=False)
        edit.event_host = user
        edit.save()
        if event.event_date_begins < datetime.date.today():
            membership = Membership.objects.get(user=user)
            if membership.posts_remaining == 0:
                messages.error(request, "Sorry, you have no posts remaining!")
                return redirect('user_profile')
            else:
                membership.posts_remaining -= 1
                membership.save()
        messages.success(request, "You have updated your event!")
        return redirect('user_profile')
    return render(request, 'post_event.html', context)

@login_required    
def delete_event(request, pk):
    """Allows Event Host to delete event"""
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    messages.success(request, "You have successfully deleted this event!")
    return redirect('user_profile')


def view_one_event(request, pk):
    """Displays event information for site user"""
    event = get_object_or_404(Event, pk=pk)
    user = request.user
    print(event.image)
    join_form = JoinEvent(request.POST or None)
    like_form = LikeEvent(request.POST or None)
    if user.is_authenticated:
        user_liked = Like.objects.filter(event=event).filter(user=user)
        user_joined = Participant.objects.filter(event=event).filter(user=user)
    else: 
        user_liked = None
        user_joined = None
    user_queue = Participant.objects.filter(event=event).count()
    current_places = event.max_participants - user_queue
    event_host = User.objects.get(id=event.event_host.id)
    # Ensures map renders at correct location
    full_address = event.address + ' ' + event.town + ' ' + event.post_code
    context = {
        'join_form': join_form,
        'like_form': like_form,
        'event': event,
        'current_places': str(current_places),
        'full_address': full_address,
        'user_joined': bool(user_joined),
        'user_liked': bool(user_liked),
        'event_host': event_host
    }
    
    # Allow user to join an event    
   
    if request.method == "POST" and 'join_form' in request.POST:
        if join_form.is_valid():
            join_form.instance.user = user
            join_form.instance.event = event
            join_form.save()
            messages.success(request, f"You have signed up for { event.title }")
            return redirect(view_one_event, pk)
        else:
            messages.error(request, f"Error: Try again later!")
    
    # Allow user to like and save an event
    
    elif request.method == "POST" and 'like_form' in request.POST:    
        if like_form.is_valid():
            like_form.instance.user = user
            like_form.instance.event = event
            like_form.save()
            messages.success(request, f"You have saved { event.title } to your like list")
            return redirect(view_one_event, pk)
        else:
            messages.error(request, f"Error: Try again later!")
      
    return render(request, 'view_one_event.html', context)
    

def delete_participant(request, pk):
    """Removes user from event"""
    event = get_object_or_404(Event, pk=pk)
    user = request.user
    participant = Participant.objects.filter(event=event).filter(user=user)
    participant.delete()
    messages.success(request, f"You are no longer booked for { event.title }")
    return redirect('search')
    
def delete_like(request, pk):
    """Removes event from user like list"""
    event = get_object_or_404(Event, pk=pk)
    user = request.user
    like = Like.objects.get(event=event, user=user)
    like.delete()
    return redirect(view_one_event, pk)
    
    
     
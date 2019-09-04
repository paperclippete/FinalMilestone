from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm, JoinEvent, LikeEvent
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalReadView
from django.urls import reverse, reverse_lazy
from .models import Event, Participant, Like

# Create your views here.
@login_required
def post_event(request):
    """Renders Create Event Form"""
    post_event_form = CreateEventForm()
    context = {
        'post_event_form': post_event_form
    }
    if request.method == "POST":
        post_event_form = CreateEventForm(request.POST)
        if post_event_form.is_valid():
            post_event_form.instance.event_host = request.user
            post_event_form.save()
            post_event_form = CreateEventForm()
        else:
            post_event_form.add_error(None, f"Oops {post_event_form.error}")
    else:    
        return render(request, 'post_event.html', context)
    
    return render(request, 'post_event.html', context)
    

def view_one_event(request, pk):
    """Displays event information for site user"""
    event = get_object_or_404(Event, pk=pk)
    user = request.user
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
    # Ensures map renders at correct location
    full_address = event.address + ' ' + event.town + ' ' + event.post_code
    context = {
        'join_form': join_form,
        'like_form': like_form,
        'event': event,
        'current_places': str(current_places),
        'full_address': full_address,
        'user_joined': bool(user_joined),
        'user_liked': bool(user_liked)
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
    return redirect('view_all_events')
    
def delete_like(request, pk):
    """Removes event from user like list"""
    event = get_object_or_404(Event, pk=pk)
    user = request.user
    like = Like.objects.filter(event=event).filter(user=user)
    like.delete()
    return render(request, 'view_one_event.html', context)
    
    
     
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm, JoinEvent
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalReadView
from django.urls import reverse, reverse_lazy
from .models import Event, Participant

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
    user_joined = Participant.objects.filter(event=event).filter(user=user)
    user_queue = Participant.objects.filter(event=event).count()
    current_places = event.max_participants - user_queue
    context = {
        'join_form': join_form,
        'event': event,
        'user_joined': user_joined,
        'current_places': str(current_places)
    }

    # Allow user to join an event    
   
    if request.method == "POST":
        if join_form.is_valid():
            join_form.instance.user = user
            join_form.instance.event = event
            join_form.save()
            messages.success(request, f"You have signed up for { event.title }")
            print(current_places)
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
    
    
     
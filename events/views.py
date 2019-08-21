from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm

# Create your views here.
@login_required
def post_event(request):
    """Renders Create Event Form"""
    post_event_form = CreateEventForm(request.POST or None)
    if post_event_form.is_valid():
        post_event_form.save()
        post_event_form = CreateEventForm()
        
    context = {
        'post_event_form': post_event_form
    }
    return render(request, 'post_event.html', context)
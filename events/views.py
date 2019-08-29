from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm

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
    

       
     
from django.shortcuts import render
from events.models import Event

# Create your views here.
def search(request):
    """Returns events searched by the user"""
    events = Event.objects.filter(title__icontains=request.GET['query'])
    context = {
        'events': events
    }
    return render(request, 'view_all_events.html', context)


def view_all_events(request):
    """Returns all events in the database"""
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'view_all_events.html', context)
    

from django.shortcuts import render
from events.models import Event

# Create your views here.

def view_events(request):
     events = Event.objects.all()
     context = {
         'events': events
     }
     return render(request, 'view_events.html', context)
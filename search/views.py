from django.shortcuts import render, redirect
from events.models import Event
from .forms import FilterEventsForm
from django.contrib import messages
import datetime


# Create your views here.
def search(request):
    """Returns events searched by the user"""
    if 'query' in request.GET:
        events = Event.objects.filter(title__icontains=request.GET['query'])
    else:
        events = Event.objects.all()
    
    filter_form = FilterEventsForm(request.POST or None)
    
    if request.method == "POST":
        if 'town' in request.POST:
            town = request.POST['town']
            if town:
                events = Event.objects.filter(town__iexact=town)
        
        if 'event_type' in request.POST:
            event_type = request.POST['event_type']
            if event_type: 
                events = Event.objects.filter(event_type__iexact=event_type)
                
        if 'day' in request.POST:
            day = request.POST['day']
            if day: 
                events = Event.objects.filter(day__iexact=day)
                
        if 'day_time' in request.POST:
            day_time = request.POST['day_time']
            if day_time: 
                events = Event.objects.filter(event_time_begins__lte='16:00:00')
                
        if 'night_time' in request.POST:
            night_time = request.POST['night_time']
            if night_time: 
                events = Event.objects.filter(event_time_begins__gt='16:00:00')
        
        if 'price' in request.POST:
            price = request.POST['price']
            if price: 
                events = Event.objects.filter(price=None)
                
    if len(events) == 0:
        messages.error(request, f"Sorry, we found 0 results! Please search again!")
        return redirect('index')
    
    context = {
        'filter_form': filter_form,
        # This will ensure no finished events appear in the search
        'events': events.exclude(event_date_ends__lt=datetime.date.today())
    }
    
    return render(request, 'view_all_events.html', context)



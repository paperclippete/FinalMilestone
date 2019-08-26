from django.urls import path, include
from .views import view_events

# Specific accounts related URLs

urlpatterns = [
    path('view_events/', view_events, name='view_events'),
    
]
from django.urls import path, include
from .views import view_all_events
from events import views

# Specific accounts related URLs

urlpatterns = [
    path('view_all_events/', view_all_events, name='view_all_events'),
    path('view_one_event/<int:pk>', views.view_one_event, name='view_one_event'),
    
]
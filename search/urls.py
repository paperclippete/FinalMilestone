from django.urls import path, include
from .views import search, view_all_events
from events import views

# Specific accounts related URLs

urlpatterns = [
    path('', search, name='search'),
    path('view_all_events/', view_all_events, name='view_all_events'),
    path('view_one_event/<int:pk>', views.view_one_event, name='view_one_event'),
    path('delete_participant/<int:pk>', views.delete_participant, name='delete_participant'),
    
]
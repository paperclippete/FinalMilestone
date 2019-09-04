from django.urls import path, include
from .views import post_event, view_one_event, delete_participant, delete_like
from events import urls_one_event

# Specific accounts related URLs

urlpatterns = [
    path('post_event/', post_event, name='post_event'),
    path('view_one_event/', include(urls_one_event)),
    
    
]
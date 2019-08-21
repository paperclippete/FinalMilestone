from django.urls import path, include
from .views import post_event

# Specific accounts related URLs

urlpatterns = [
    path('post_event/', post_event, name='post_event'),
    
]
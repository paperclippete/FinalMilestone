from django.urls import path, include
from .views import search, view_all_events


# Specific accounts related URLs

urlpatterns = [
    path('', search, name='search'),
    path('view_all_events/', view_all_events, name='view_all_events'),
   
]
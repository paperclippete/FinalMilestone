from django.urls import path, include
from .views import search


# Specific accounts related URLs

urlpatterns = [
    path('', search, name='search'),
    
]
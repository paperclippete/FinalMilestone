from django.urls import path, include
from .views import membership


# Specific accounts related URLs

urlpatterns = [
    path('upgrade/', membership, name='membership'),
    
]
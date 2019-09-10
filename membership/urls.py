from django.urls import path, include
from .views import membership


# Specific accounts related URLs

urlpatterns = [
    path('upgrade/<str:membership_level>/', membership, name='membership'),
    
]
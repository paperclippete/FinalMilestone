from django.urls import path
from accounts.views import logout, login

# Specific accounts related URLs

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    
]
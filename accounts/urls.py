from django.urls import path
from accounts.views import logout

# Specific accounts related URLs

urlpatterns = [
    path('logout/', logout, name="logout"),
    
]
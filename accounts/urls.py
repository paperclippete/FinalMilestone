from django.urls import path
from accounts.views import logout, login, register, user_profile

# Specific accounts related URLs

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user_profile'),

]
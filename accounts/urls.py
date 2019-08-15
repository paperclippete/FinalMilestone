from django.urls import path, include
from accounts.views import logout, login, register, user_profile
from accounts import urls_reset

# Specific accounts related URLs

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user_profile'),
    path('password-reset/', include(urls_reset))
]
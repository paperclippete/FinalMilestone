from django.urls import path, include
from .views import logout, login, login_modal, register, user_profile
from accounts import urls_reset

# Specific accounts related URLs

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login_modal/', login_modal, name='login_modal'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user_profile'),
    path('password-reset/', include(urls_reset))
]
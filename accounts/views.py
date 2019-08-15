from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.

def index(request):
    """Return index.html as homepage"""
    return render(request, 'index.html')

    
def logout(request):
    """Logout user and end session"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))

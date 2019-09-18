from django.shortcuts import render, redirect
from accounts.forms import UserLoginForm


# Create your views here.

def index(request):
    """Return index.html as homepage"""
    return render(request, 'index.html')
    
def about_us(request):
    """Return about_us.html"""
    return render(request, 'about_us.html')
    

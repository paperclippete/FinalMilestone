from django.shortcuts import render

# Create your views here.

def index(request):
    """Return index.html as homepage"""
    return render(request, 'index.html')
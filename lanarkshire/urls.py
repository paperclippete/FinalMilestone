"""lanarkshire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from home.views import index, about_us
from accounts import urls as urls_accounts
from events import urls as urls_events
from search import urls as urls_search
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about_us/', about_us, name='about_us'),
    path('accounts/', include(urls_accounts)),
    path('events/', include(urls_events)),
    path('search/', include(urls_search)),
    re_path(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]

from django.contrib import admin
from .models import Event, Participant, Like

# Register your models here.

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Like)
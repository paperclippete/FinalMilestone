from django.contrib import admin
from .models import Membership, Order

# Register your models here.
admin.site.register(Membership)
admin.site.register(Order)
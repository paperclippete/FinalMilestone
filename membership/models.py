from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Membership(models.Model):
    """User membership of site"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bronze = models.BooleanField(default=True)
    silver = models.BooleanField(null=True)
    gold = models.BooleanField(null=True)
    posts_remaining = models.IntegerField(default=0)
    
    
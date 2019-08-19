from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    """A User created Event"""
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    age_range = models.CharField(max_length=12)
    town = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    post_code = models.CharField(max_length=60)
    event_type = models.CharField(max_length=60)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_host = models.ForeignKey(User, on_delete=models.CASCADE)
    max_participants = models.IntegerField()
    image = models.ImageField(upload_to="event_images", blank=True)
    
    def __str__(self):
        return self.title
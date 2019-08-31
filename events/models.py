from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Event(models.Model):
    """A User created Event"""
    
    # Choice selections
    AGE_RANGE_CHOICES = [
        (None, 'Please Choose'),
        ('Babies and Toddlers', 'Babies and Toddlers'),
        ('Children', 'Children'),
        ('Teenagers', 'Teenagers'),
        ('Adults', 'Adults'),
        ('OAPs', 'OAPs')
    ]
    TOWN_CHOICES = [
        (None, 'Please Choose'),
        ('Airdrie', 'Airdrie'),
        ('Bellshill', 'Bellshill'),
        ('Biggar', 'Biggar'),
        ('Carluke', 'Carluke'),
        ('Coatbridge', 'Coatbridge'),
        ('East Kilbride', 'East Kilbride'),
        ('Hamilton', 'Hamilton'),
        ('Lanark', 'Lanark'),
        ('Larkhall', 'Larkhall'),
        ('Lesmahagow', 'Lesmahagow'),
        ('Motherwell', 'Motherwell'),
        ('Rutherglen', 'Rutherglen'),
        ('Strathaven', 'Strathaven'),
        ('Wishaw', 'Wishaw'),
    ]
    EVENT_TYPE_CHOICES = [
        (None, 'Please Choose'),
        ('Arts and Crafts', 'Arts and Crafts'),
        ('Educational', 'Educational'),
        ('Nature', 'Nature'),
        ('Entertainment', 'Entertainment'),
        ('Health and Wellbeing', 'Health and Wellbeing'),
        ('Physical and Exercise', 'Physical and Exercise')
    ]
    DAY_CHOICES = [
        (None, 'Please Choose'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    age_range = models.CharField(max_length=20, choices=AGE_RANGE_CHOICES, blank=False, default="Please Choose")
    town = models.CharField(max_length=20, choices=TOWN_CHOICES, blank=False, default="Please Choose")
    address = models.CharField(max_length=60)
    post_code = models.CharField(max_length=8)
    event_type = models.CharField(max_length=40, choices=EVENT_TYPE_CHOICES, blank=False, default="Please Choose")
    event_date_begins = models.DateField()
    event_date_ends = models.DateField()
    event_day = models.CharField(max_length=20, choices=DAY_CHOICES, blank=False, default="Please Choose")
    event_time_begins = models.TimeField()
    event_time_ends = models.TimeField()
    event_host = models.ForeignKey(User, on_delete=models.CASCADE)
    max_participants = models.IntegerField()
    image = models.ImageField(upload_to="images", blank=True)
    
    def __str__(self):
        return self.title
        
        
class Participant(models.Model):
    """User Joins and Event"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0} joined {1}".format(
            self.user.email, self.event.title)
    
    
        

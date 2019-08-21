from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    """A User created Event"""
    
    # Choice selections
    AGE_RANGE_CHOICES = [
        ('Babies and Toddlers', 'Babies and Toddlers'),
        ('Children', 'Children'),
        ('Teenagers', 'Teenagers'),
        ('Adults', 'Adults'),
        ('OAPs', 'OAPs')
    ]
    TOWN_CHOICES = [
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
        ('Arts and Crafts', 'Arts and Crafts'),
        ('Educational', 'Educational'),
        ('Nature', 'Nature'),
        ('Entertainment', 'Entertainment'),
        ('Health and Wellbeing', 'Health and Wellbeing'),
        ('Physical and Exercise', 'Physical and Exercise')
    ]
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    age_range = models.CharField(max_length=20, choices=AGE_RANGE_CHOICES, blank=False, default="Please Choose")
    town = models.CharField(max_length=20, choices=TOWN_CHOICES, blank=False, default="Please Choose")
    address = models.CharField(max_length=60)
    post_code = models.CharField(max_length=8)
    event_type = models.CharField(max_length=40, choices=EVENT_TYPE_CHOICES, blank=False, default="Please Choose")
    event_date = models.DateField()
    event_time = models.TimeField()
    event_host = models.ForeignKey(User, on_delete=models.CASCADE)
    max_participants = models.IntegerField()
    image = models.ImageField(upload_to="event_images", blank=True)
    
    def __str__(self):
        return self.title
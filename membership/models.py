from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Membership(models.Model):
    """User membership of site"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bronze = models.BooleanField(default=True, null=True)
    silver = models.BooleanField(null=True)
    gold = models.BooleanField(null=True)
    posts_remaining = models.IntegerField(default=0)


class Order(models.Model):
    """When a user purchases a membership"""
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=6, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    date = models.DateTimeField(blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.user.id)

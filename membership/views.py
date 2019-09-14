from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Membership, Order
from .forms import OrderMembershipForm
from django.utils import timezone
from django.conf import settings
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required
def membership(request, membership_level):
    """Returns membership upgrade with payment"""
    order_form = OrderMembershipForm(request.POST)
    user = request.user
    membership = Membership.objects.get(user=user)
    if request.method == "POST" and order_form.is_valid():
        print(request.POST)
        membership.bronze = True if membership_level == 'bronze' else False
        membership.silver = True if membership_level == 'silver' else False
        membership.gold = True if membership_level == 'gold' else False
        membership.posts_remaining = 0 if membership_level == 'bronze' else 2 if membership_level == 'silver' else 15
        membership.save()
        order = order_form.save(commit=False)
        order.membership = membership
        order.user = user
        order.level = membership_level
        order.date = timezone.now()
        order.save()
        price = 20 if membership_level == 'silver' else 120
        try:
            token = request.POST['stripeToken']
            customer = stripe.Charge.create(
                amount = int(price * 100),
                currency = "GBP",
                description = request.user.email,
                source=token,
            )
        except stripe.error.CardError:
            messages.error(request, "Sorry, your card was declined!")
                
        if customer.paid:
            messages.success(request, "You have successfully paid!")
            return redirect(reverse('user_profile'))
        else:
            messages.error(request, "Unable to take payment, try again!")
    
    return redirect(reverse('user_profile'))
    
    
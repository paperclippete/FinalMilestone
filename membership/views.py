from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Membership, Order
from .forms import MakePaymentForm, OrderMembershipForm
from django.contrib import messages
from django.conf import settings
import stripe
from django.utils import timezone

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

def membership(request, membership_level):
    """Returns membership upgrade form with payment facility"""
    payment_form = MakePaymentForm(request.POST or None)
    order_form = OrderMembershipForm(request.POST or None)
    # order_form(instance=request.user)
    user = request.user
    if request.method == "POST":
        print(request.POST)
        if membership_level == 'bronze':
            if order_form.is_valid():
                membership = Membership.objects.get(user=user)
                membership.bronze = True
                membership.silver = False
                membership.gold = False
                membership.posts_remaining = 0
                membership.save()
                print('membership done')
                order = order_form.save(commit=False)
                order.membership = membership
                order.user = user
                order.level = membership_level
                order.date = timezone.now()
                order.save()
                print('order done')
                messages.success(request, "You are now a Bronze member!")
                return redirect(reverse('user_profile'))
        # elif membership_level == 'silver':    
        #     if order_form.is_valid() and payment_form.is_valid():
        #         membership = Membership.objects.get(user=user)
        #         membership.bronze = False
        #         membership.silver = True
        #         membership.gold = False
        #         membership.posts_remaining = 2
        #         membership.save()
        #         order = order_form.save(commit=False)
        #         order.membership = membership
        #         order.user = user
        #         order.level = membership_level
        #         order.save()
        #         try:
        #             customer = stripe.Charge.create(
        #                 amount = int(20 * 100),
        #                 currency = "GBP",
        #                 description = request.user.email,
        #                 card = payment_form.cleaned_data['stripe_id'],
        #             )
        #         except stripe.error.CardError:
        #             messages.error(request, "Your card was declined!")
                
        # if membership_level == 'gold':
    
    
        # membership = Membership.objects.create
        
        # order = order_form.save(commit=False)
        # order.date = timezone.now()
        # order.save()
    
    
    context = {
        'membership_level': membership_level,
        'payment_form': payment_form,
        'order_form': order_form,
    }
    return render(request, 'membership.html', context)
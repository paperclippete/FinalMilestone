from django import forms
from .models import Membership, Order

class MakePaymentForm(forms.Form):
    """Form handles payment for user membership upgrade"""
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2026)]

    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderMembershipForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['membership', 'user', 'date', 'level']
        labels = {
            "street_address1": "Address Line 1",
            "street_address2": "Address Line 2"
        }
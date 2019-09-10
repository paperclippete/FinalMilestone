from django import forms
from .models import Membership, Order

class MakePaymentForm(forms.Form):
    """Form handles payment for user membership upgrade"""
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderMembershipForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['membership', 'user', 'date', 'level']
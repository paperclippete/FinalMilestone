from django import forms
from .models import Membership, Order

class OrderMembershipForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['membership', 'user', 'date', 'level']
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "town_or_city": "Town or City",
            "street_address1": "Address Line 1",
            "street_address2": "Address Line 2"
        }

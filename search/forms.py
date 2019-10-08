from django import forms
from events.models import TOWN_CHOICES, EVENT_TYPE_CHOICES, DAY_CHOICES, AGE_RANGE_CHOICES


class FilterEventsForm(forms.Form):
    town = forms.ChoiceField(label='Location', required=False, choices=TOWN_CHOICES)
    event_type = forms.ChoiceField(label='Type of Event', required=False, choices=EVENT_TYPE_CHOICES)
    day = forms.ChoiceField(label='Day', required=False, choices=DAY_CHOICES)
    age_range = forms.ChoiceField(label='Age', required=False, choices=AGE_RANGE_CHOICES)
    day_time = forms.BooleanField(label='Day Events', required=False)
    night_time = forms.BooleanField(label='Evening Events', required=False)
    price = forms.BooleanField(label='Free Events', required=False)


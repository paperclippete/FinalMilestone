from django import forms
from .models import Event
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class CreateEventForm(forms.ModelForm):
    """Form for creating events"""
    description = forms.CharField(widget=forms.Textarea)
    event_date = forms.DateField(widget=DatePickerInput(format='%d/%m/%Y'))
    event_time = forms.TimeField(widget=TimePickerInput())

    class Meta:
        model = Event
        exclude = ['event_host'] 
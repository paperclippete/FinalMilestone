from django import forms
from .models import Event
import datetime
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class CreateEventForm(forms.ModelForm):
    """Form for creating events"""
    description = forms.CharField(widget=forms.Textarea)
    event_date = forms.DateField(input_formats=["%d/%m/%Y"], widget=DatePickerInput(format='%d/%m/%Y').start_of('app'))
    event_time = forms.TimeField(widget=TimePickerInput())

    class Meta:
        model = Event
        exclude = ['event_host'] 
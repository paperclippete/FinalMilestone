from django import forms

class UserLoginForm(forms.Form):
    """Form for User Login"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
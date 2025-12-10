from django import forms
from .models import *

class register_form(forms.ModelForm):
    class Meta:
        model=user_register
        fields ='__all__'

class artist_booking_form(forms.ModelForm):
    class Meta:
        model = book_artist_cls
        exclude = ['user']

class feedback_form(forms.ModelForm):
    class Meta:
        model = feedback_cls
        fields = ['feedback']

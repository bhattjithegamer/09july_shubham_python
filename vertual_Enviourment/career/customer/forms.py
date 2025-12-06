from django import forms
from .models import *

class register_form(forms.ModelForm):
    class Meta:
        model=user_register
        fields ='__all__'
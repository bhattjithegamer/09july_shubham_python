from django import forms
from .models import *

class signupform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = '__all__'
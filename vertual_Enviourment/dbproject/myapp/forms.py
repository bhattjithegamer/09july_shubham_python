from django import forms
from .models import *

class userform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = '__all__'
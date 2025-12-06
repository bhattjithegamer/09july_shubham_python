from django import forms
from .models import *

class signupform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = '__all__'

class notesform(forms.ModelForm):
    class Meta:
        model=mynotes
        fields=['title','desc','subject','files']

class contactform(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'



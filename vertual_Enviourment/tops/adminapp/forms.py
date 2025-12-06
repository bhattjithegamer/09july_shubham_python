from .models import *
from django import forms
from myapp.models import *


class notesform(forms.ModelForm):
    class Meta:
        model = mynotes
        fields = ['title', 'description', 'subject', 'file']

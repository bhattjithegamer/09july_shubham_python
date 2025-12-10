from django import forms
from .models import *


class artist_form(forms.ModelForm):
    class Meta:
        model=register_artist
        fields='__all__'

class artist_file_form(forms.ModelForm):
    class Meta:
        model=file_artist
        fields = ['file']

class artist_feedback_form(forms.ModelForm):
    class Meta:
        model = feedback_artist_cls
        fields = ['feedback']

 
from django import forms
from .models import *


class artist_form(forms.ModelForm):
    class Meta:
        model=register_artist
        fields='__all__'
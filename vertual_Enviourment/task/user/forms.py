from django import forms
from .models import *


class userloginform(forms.ModelForm):
    class Meta:
        model=userlogin
        fields="__all__"

class postform(forms.ModelForm):
    class Meta:
        model=post
        fields="__all__"
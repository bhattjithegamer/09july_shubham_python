from django import forms
from .models import *

class user_register_form(forms.ModelForm):
    class Meta:
        model = user_register
        fields = '__all__'

class contact_form(forms.ModelForm):
    class Meta:
        model = contact_cls
        fields = '__all__'

class payment_form(forms.ModelForm):
    class Meta:
        model = payment_cls
        fields = ['debit_card_number', 'mm_yy', 'cvv', 'upi_id']

    def __init__(self, *args, **kwargs):
        super(payment_form, self).__init__(*args, **kwargs)
        self.fields['debit_card_number'].required = False
        self.fields['mm_yy'].required = False
        self.fields['cvv'].required = False
        self.fields['upi_id'].required = False
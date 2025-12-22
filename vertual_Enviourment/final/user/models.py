from django.db import models
from adminapp.models import *

# Create your models here.

class user_register(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

class Cart(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

class contact_cls(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField() 

class payment_cls(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0.0) 
    debit_card_number = models.CharField(max_length=20, null=True, blank=True)
    mm_yy = models.CharField(max_length=5, null=True, blank=True)
    cvv = models.CharField(max_length=4, null=True, blank=True)
    upi_id = models.CharField(max_length=100, null=True, blank=True)
    cash_on_delivery = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class wishlist(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
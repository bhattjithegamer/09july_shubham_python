from django.db import models

# Create your models here.

class UserSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    mobile=models.BigIntegerField()
    
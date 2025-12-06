from django.db import models

# Create your models here.

class user_register(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    mobile=models.IntegerField(max_length=10)

# class manage_profille(models.Model):

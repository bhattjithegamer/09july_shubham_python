from django.db import models

# Create your models here.

class register_artist(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.IntegerField(max_length=100)
    category=models.CharField(max_length=100)
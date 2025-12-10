from django.db import models
from customer.models import *

# Create your models here.

class register_artist(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    status_opt=[
        ('Pending','Pending'),
        ('Approve','Approve'),
        ('Reject','Reject')
    ]
    status=models.CharField(max_length=20,choices=status_opt)



class file_artist(models.Model):
    user=models.ForeignKey(register_artist,on_delete=models.CASCADE)
    file=models.FileField()

class feedback_artist_cls(models.Model):
    user=models.ForeignKey(register_artist,on_delete=models.CASCADE)
    feedback = models.CharField()


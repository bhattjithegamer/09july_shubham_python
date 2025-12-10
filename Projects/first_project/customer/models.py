from django.db import models
import datetime

# Create your models here.

class user_register(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    def __str__(self):
        return self.fullname  # Ahiya customer nu naam return karo

class book_artist_cls(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)  # customer
    artistname = models.CharField(max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=100)
    status_opt = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]

    status = models.CharField(max_length=20, choices=status_opt, default='Pending')


class feedback_cls(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    feedback=models.CharField()


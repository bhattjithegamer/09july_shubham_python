from django.db import models

# Create your models here.

class user_register(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    mobile=models.IntegerField(max_length=10)
    def __str__(self):
        return self.fullname  # Ahiya customer nu naam return karo

class book_artist_cls(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)  # customer
    artistname = models.CharField(max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=100)


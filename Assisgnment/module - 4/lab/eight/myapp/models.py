from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()
    hospital = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

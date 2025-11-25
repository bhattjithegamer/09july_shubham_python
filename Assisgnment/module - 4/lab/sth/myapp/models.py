from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

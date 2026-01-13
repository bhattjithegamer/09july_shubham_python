from django.db import models

class DoctorProfile(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
from django.db import models
from django.utils import timezone


# Create your models here.

class CrimeData(models.Model):
    crime_id = models.AutoField(primary_key=True)
    crime_type = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    frequency = models.IntegerField()

    def __str__(self):
        return f"{self.crime_type} at {self.location} on {self.date}"


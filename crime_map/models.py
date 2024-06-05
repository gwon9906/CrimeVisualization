from django.db import models

# Create your models here.
class CrimeData(models.Model):
    crime_type = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=255)
    frequency = models.IntegerField()

    def __str__(self):
        return f"{self.crime_type} at {self.location} on {self.date}"
from django.db import models

class CrimeData(models.Model):
    station = models.CharField(max_length=100)
    crime_type = models.CharField(max_length=100)
    year = models.IntegerField()
    murder = models.IntegerField(default=0)
    robbery = models.IntegerField(default=0)
    sexual_crime = models.IntegerField(default=0)
    theft = models.IntegerField(default=0)
    violence = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.station} - {self.crime_type} - {self.year}"

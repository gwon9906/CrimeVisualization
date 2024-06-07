from django.db import models

class CrimeData(models.Model):
    station = models.CharField(max_length=100)
    crime_type = models.CharField(max_length=100)
    year = models.IntegerField()
    murder = models.IntegerField()
    robbery = models.IntegerField()
    sexual_crime = models.IntegerField()
    theft = models.IntegerField()
    violence = models.IntegerField()

    def __str__(self):
        return f"{self.station} - {self.crime_type} - {self.year}"

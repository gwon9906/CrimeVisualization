from django.db import models

class CrimesCrimedata(models.Model):
    id = models.BigAutoField(primary_key=True)
    station = models.CharField(max_length=100)
    crime_type = models.CharField(max_length=100)
    year = models.IntegerField()
    murder = models.IntegerField()
    robbery = models.IntegerField()
    sexual_crime = models.IntegerField()
    theft = models.IntegerField()
    violence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crimes_crimedata'

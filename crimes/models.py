from django.db import models
from django.utils import timezone

# Create your models here.
class Crime(models.Model):
    date = models.DateTimeField()
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.category


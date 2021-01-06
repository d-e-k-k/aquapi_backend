from django.db import models

# Create your models here.

class Temperature(models.Model):
    temperature = models.FloatField()
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    def __str__(self):
        return str(self.temperature)
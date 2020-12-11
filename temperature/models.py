from django.db import models

# Create your models here.

class Temperature(models.Model):
    temperature = models.SmallIntegerField()
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.temperature} at {self.time} on {self.date}'
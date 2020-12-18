from django.db import models

# Create your models here.

class WaterChange(models.Model):
    water_change_date = models.DateField(auto_now_add=True, auto_now=False)
    time_stamp = models.DateField(auto_now_add=True, auto_now=False)
    completed = models.BooleanField()
    water_change_interval = models.PositiveSmallIntegerField()

    def __str__(self):
        return (f'Last Water Change was on: {self.water_change_date}  Interval: {self.water_change_interval} days')

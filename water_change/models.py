from django.db import models

# Create your models here.

class WaterChange(model.Models):
    water_change_date = models.DateField(auto_now_add=True, auto_now=False)
    water_change_interval = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Last Water Change was on: {water_change_date}  Interval: {water_change_interval} days'

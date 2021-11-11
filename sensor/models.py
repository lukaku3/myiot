from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class Sensor(models.Model):
    sensor_type = models.PositiveSmallIntegerField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __int__(self):
        return self.sensor_type
    def __float__(self):
        return self.temperature
    def __float__(self):
        return self.pressure
    def __float__(self):
        return self.humidity
    def __str__(self):
        return self.created_at
    def __str__(self):
        return self.updated_at

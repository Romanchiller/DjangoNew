from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.RESTRICT, related_name='measurements')
    temperature = models.SmallIntegerField(default= 0)
    datetime = models.DateTimeField(auto_now_add=True)


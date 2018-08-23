from django.db import models

# Create your models here.

class Flights(models.Model):
    source = models.CharField(max_length = 20)
    dest = models.CharField(max_length = 20)

    def __str__(self):
        return self.source


class FlightTypes(models.Model):

	#change it to appropriate field types !

    code = models.CharField(max_length = 6)
    flight_name = models.CharField(max_length = 20)
    dept_time=models.CharField(max_length = 10)
    arrival_time=models.CharField(max_length = 10)
    price=models.CharField(max_length = 10)
    duration=models.CharField(max_length = 10)

    def __str__(self):
        return self.flight_name
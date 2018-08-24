from django.db import models

# Create your models here.

class Flights(models.Model):
    source = models.CharField(max_length = 20)
    dest = models.CharField(max_length = 20)

    def __str__(self):
        return self.source


class FlightTypes(models.Model):


    code = models.CharField(max_length = 6)
    flight_name = models.CharField(max_length = 20)
    dept_time=models.CharField(max_length = 10)
    arrival_time=models.CharField(max_length = 10)
    price=models.CharField(max_length = 10)
    duration=models.CharField(max_length = 10)

    def __str__(self):
        return self.flight_name

class Passenger(models.Model):
    p_name=models.CharField(max_length = 20)
    source = models.CharField(max_length = 20)
    dest = models.CharField(max_length = 20)
    seats= models.CharField(max_length = 1)
    date=models.CharField(max_length = 10)
    code = models.CharField(max_length = 6)
    flight_name = models.CharField(max_length = 20)
    dept_time=models.CharField(max_length = 10)
    arrival_time=models.CharField(max_length = 10)
    price=models.CharField(max_length = 10)
    duration=models.CharField(max_length = 10)
    def __str__(self):
        return self.p_name

    class Meta:
        get_latest_by = 'id'
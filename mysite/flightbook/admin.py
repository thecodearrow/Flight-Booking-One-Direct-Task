from django.contrib import admin
from .models import Flights,FlightTypes,Passenger

# Register your models here.

admin.site.register(Flights)
admin.site.register(FlightTypes)
admin.site.register(Passenger)
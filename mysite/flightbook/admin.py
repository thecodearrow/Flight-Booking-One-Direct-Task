from django.contrib import admin
from .models import Flights,FlightTypes

# Register your models here.

admin.site.register(Flights)
admin.site.register(FlightTypes)
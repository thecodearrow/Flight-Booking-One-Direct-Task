from django.shortcuts import render
from .models import Flights,FlightTypes

def index(request):
    flights=Flights.objects.all() #passing Flights QuerySet
    return render(request, 'index.html',{'flights':flights})

def landing(request):
    flight_types1=FlightTypes.objects.get(code="#BUS12") 
    flight_types2=FlightTypes.objects.get(code="#ECO12")
    return render(request, 'landing.html',{'business':flight_types1,'economy':flight_types2})
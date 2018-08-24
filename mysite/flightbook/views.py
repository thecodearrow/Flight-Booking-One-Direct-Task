from django.shortcuts import render
from .models import Flights,FlightTypes,Passenger

def index(request):
    flights=Flights.objects.all() #passing Flights QuerySet
    return render(request, 'index.html',{'flights':flights})

def landing(request):
    flight_types1=FlightTypes.objects.get(code="#BUS12") 
    flight_types2=FlightTypes.objects.get(code="#ECO12")
    passenger=Passenger.objects.create()
    obtained=request.GET 
    #saving details to database
    if('person_name' in obtained):
        passenger.p_name=request.GET['person_name']
    if('start' in obtained):
        passenger.source=request.GET['start']
    if('end' in obtained):
        passenger.dest=request.GET['end']

    if('date-travel' in obtained):
        passenger.date=request.GET['date-travel']

    if('seats' in obtained):
        passenger.seats=request.GET['seats']
    passenger.save() #save to database

    return render(request, 'landing.html',{'business':flight_types1,'economy':flight_types2})

def confirmed(request):
    passenger=Passenger.objects.latest() #passing Latest passenger details
    business=FlightTypes.objects.get(code="#BUS12") 
    economy=FlightTypes.objects.get(code="#ECO12")
    obtained=request.GET 
    if("business" in obtained):
        
        passenger.code=business.code
        
        passenger.flight_name=business.flight_name
        
        passenger.dept_time=business.dept_time

        passenger.arrival_time=business.arrival_time

        passenger.price=business.price

        passenger.duration=business.duration
    if("economy" in obtained):
        
        passenger.code=economy.code
        
        passenger.flight_name=economy.flight_name
        
        passenger.dept_time=economy.dept_time

        passenger.arrival_time=economy.arrival_time

        passenger.price=economy.price

        passenger.duration=economy.duration

    passenger.save() #save to database

    return render(request, 'confirmed.html',{'passenger':passenger})
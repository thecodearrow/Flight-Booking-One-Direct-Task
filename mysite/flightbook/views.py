from django.shortcuts import render
from .models import Flights

def index(request):
    flights=Flights.objects.all() #passing Flights QuerySet
    return render(request, 'index.html',{'flights':flights})
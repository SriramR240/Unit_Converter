from django.shortcuts import render
from django.http import HttpResponse

def temperatureform(request):
    return render(request,'temperature.html')


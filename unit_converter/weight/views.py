from django.shortcuts import render
from django.http import HttpResponse

def weightform(request):
    return render(request,'weight.html')

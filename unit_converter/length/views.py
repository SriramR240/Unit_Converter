from django.shortcuts import render
from django.http import HttpResponse

def lengthform(request):
    return render(request,'length.html')



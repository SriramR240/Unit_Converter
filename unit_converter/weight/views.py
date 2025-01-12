from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("..")
from utils.forms import UnitForm , getFormData


conversion = {'milligram': 1e6, 'gram': 1e3, 'kilogram': 1, 'pound': 2.205,'ounce':35.27}

def weightform(request):

    if request.method=='POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            result = getFormData(form,conversion)
            return render(request, 'weight.html', context={'converted_value': result})
    else:
        result = ''
        return render(request,'weight.html', context = {'converted_value' : result })

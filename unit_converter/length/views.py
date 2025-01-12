from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("..")
from utils.forms import UnitForm , getFormData

conversion = {'kilometer': 1, 'meter': 1e3, 'centimeter': 1e5, 'millimeter': 1e6,
              'inch': 39370.1, 'foot': 3280.84167, 'yard': 1093.61, 'mile': 0.54}

def lengthform(request):

    if request.method=='POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            result = getFormData(form,conversion)
            return render(request, 'length.html', context={'converted_value': result})
    else:
        result = ''
        return render(request,'length.html', context = {'converted_value' : result })



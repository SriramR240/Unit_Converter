from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("..")
from utils.forms import UnitForm , getFormData,getFormDataTemp




def temperatureform(request):
    if request.method=='POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            result = getFormDataTemp(form)
            return render(request, 'temperature.html', context={'converted_value': result})
    else:
        result = ''
        return render(request,'temperature.html', context = {'converted_value' : result })


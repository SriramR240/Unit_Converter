from django import forms


class UnitForm(forms.Form):
    value = forms.IntegerField(label="Enter value:")
    fromUnit = forms.CharField(label='From:')
    toUnit = forms.CharField(label='To:')

def getFormData(form,conversion):
    value = form.cleaned_data["value"]
    fromUnit = form.cleaned_data["fromUnit"]
    toUnit = form.cleaned_data['toUnit']
    result = (conversion[toUnit] / conversion[fromUnit]) * value

    return result

def getFormDataTemp(form):
    value = form.cleaned_data["value"]
    fromUnit = form.cleaned_data["fromUnit"]
    toUnit = form.cleaned_data['toUnit']

    if fromUnit == "Celsius":
        if toUnit == "Fahrenheit":
            result = (value* (9/5))+32
        elif toUnit == 'Kelvin':
            result = value + 273.15
        else:
            result =value
    elif fromUnit == "Fahrenheit":
        if toUnit == "Celsius":
            result = (value -32) *(5/9)
        elif toUnit == "Kelvin":
            result = (value - 32) * (5 / 9) + 273.15
        else:
            result =value
    else:
        if toUnit == "Celsius":
            result = value - 273.15
        elif toUnit == "Fahrenheit":
            result = (value - 273.15) * (9/5) + 32
        else:
            result =value
    return result
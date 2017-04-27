from django import forms
from .models import Employee
from django.forms.widgets import NumberInput

class EmployeeForm(forms.ModelForm):
    pincode = forms.IntegerField(min_value = 100000, widget = forms.NumberInput(attrs={'min':100000, 'max': 999999,}))

    class Meta:
        model = Employee
        exclude = ['emp_id',]
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_no', 'employee_name', 'email_id', 'mobile_no', 'salary']

from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import employee, customer


class NewUser(UserCreationForm):
    pass


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        exclude = []
        pass
    pass


class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        exclude = []
        pass
    pass

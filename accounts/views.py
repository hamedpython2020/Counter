from django.shortcuts import render

# Create your views here.
from accounts.forms import EmployeeForm, CostumerForm


def Newemployee(request):
    if request.method == 'POST':
        context = {

        }
    else:
        employee = EmployeeForm()
        context = {
            'employee': employee
        }
    return render(request, 'accounts/new_employee.html', context)


def Newcostumer(request):
    if request.method == 'POST':
        context = {

        }
    else:
        costumer = CostumerForm()
        context = {
            'costumer': costumer
        }
    return render(request,'accounts/new_costumer.html', context)

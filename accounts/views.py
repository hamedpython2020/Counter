from django.shortcuts import render

# Create your views here.
from accounts.forms import EmployeeForm, CustomerForm


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


def Newcustomer(request):
    if request.method == 'POST':
        context = {

        }
    else:
        customer = CustomerForm()
        context = {
            'customer': customer
        }
    return render(request, 'accounts/new_customer.html', context)

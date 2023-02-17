from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from accounts.forms import EmployeeForm, CustomerForm, NewUser, PayForm
from accounts.models import payment


def index(request):
    return render(request, 'accounts/index.html', context={})


    ################## New user and complete Profile {employee , customer} ############
def Newemployee(request):
    if request.method == 'POST':
        employee = EmployeeForm(request.POST)
        if employee.is_valid():
            employee.save()
            user = request.user
            user.staff = True
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


    ###################    user Registrations ########################
def Signup(request):
    if request.method == 'POST':
        context = {}
    else:
        user = NewUser()
        context = {
            'user': user
        }
    return render(request, 'accounts/signup.html', context)


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is None:
            context = {
                'username': username,
                'error': 'موجود نیست'
            }
        else:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                return HttpResponseRedirect(reverse(viewname='index'))
            pass
        pass
    else:
        context = {}
    return render(request, "accounts/login.html", context)


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(viewname='login'))


    ################## Payment views {list , creat } ####################
def NewPayment(request):
    if request.method == 'POST':
        pay = PayForm(request.POST)
        if pay.is_valid():
            pay.save()
            return HttpResponseRedirect(reverse(viewname='payment_list'))
        context = {

        }
        pass
    else:
        pay = PayForm()
        context = {
            'pay': pay
        }
    return render(request, 'accounts/payment.html', context)


def Paymentlist(request):
    try:
        pay = payment.objects.all().order_by('date')
        context = {
            'pay': pay
        }
    except:
        error = 'Something wrong'
        context = {
            'error': error
        }
        pass
    return render(request, 'accounts/payment_list.html', context)



    pass


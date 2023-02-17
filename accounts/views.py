from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from accounts.forms import EmployeeForm, CustomerForm, NewUser, PayForm
from accounts.models import payment, employee, customer

def index(request):
    return render(request, 'accounts/index.html', context={})


    ################## New user and complete Profile {employee , customer} ############


def Newemployee(request):
    if request.method == 'POST':
        employee = EmployeeForm(request.POST, request.FILES)
        if employee.is_valid():
            user = request.user
            user.is_staff = True
            user.save()
            employee.save()

            return HttpResponseRedirect(reverse('index'))
        context = {}
    else:
        employee = EmployeeForm()
        context = {
            'employee': employee
        }
    return render(request, 'accounts/new_employee.html', context)


def Employee(request, employee_id):
    prof = employee.objects.get(id=employee_id)
    context = {
       'prof': prof
    }
    return render(request, 'accounts/employee.html', context)


def Newcustomer(request):
    if request.method == 'POST':
        customer = CustomerForm(request.POST, request.FILES)
        if customer.is_valid():
            customer.save()
            return HttpResponseRedirect(reverse('works:project_new'))
        else:
            context = {
                'error': 'we have wrong here'
            }
    else:
        customer = CustomerForm()
        context = {
            'customer': customer
        }
    return render(request, 'accounts/new_customer.html', context)


def Customer(request, customer_id):
    customer = employee.objects.get(id=customer_id)
    context = {
       'customer': customer
    }
    return render(request, 'accounts/customer.html', context)


def Customerlist(request):
    obj = customer.objects.all().order_by('l_name')
    obj_c = obj.count()
    context = {
        'obj': obj,
        'obj_c': obj_c
    }
    return render(request, 'accounts/customer_list.html', context)


################## User Registrations ####################

def Signup(request):
    if request.user is not None:
        logout(request)
        pass
    if request.method == 'POST':
        user = NewUser(request.POST)
        if user.is_valid():
            user = user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:new_employee'))
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
    return HttpResponseRedirect(reverse('accounts:login'))


################## Payment views {list , creat } ####################
def NewPayment(request):
    if request.method == 'POST':
        pay = PayForm(request.POST)
        if pay.is_valid():
            pay = pay.save()
            value = pay.value
            customer = pay.manager
            customer.pay_service(value)
            customer.save()
            pay.save()
            return HttpResponseRedirect(reverse('accounts:payment_list'))
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
        pay_c = pay.count()
        context = {
            'pay': pay,
            'pay_c': pay_c
        }
    except:
        error = 'Something is wrong'
        context = {
            'error': error
        }
        pass
    return render(request, 'accounts/payment_list.html', context)


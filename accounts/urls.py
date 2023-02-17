from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('employee/new/', views.Newemployee, name='new_employee'),
    path('employee/<int:employee_id>/', views.Employee, name='employee'),
    path('payment/new/', views.NewPayment, name='new_payment'),
    path('payment/list/', views.Paymentlist, name='payment_list'),
    path('signup/', views.Signup, name='signup'),
    path('customer/new/', views.Newcustomer, name='new_customer'),
    path('customer/<int:customer_id>/', views.Customer, name='customer'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),


]
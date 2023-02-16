from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('employee/new', views.Newemployee, name='new_employee'),
    path('signup/', views.Signup, name='signup'),
    path('customer/new', views.Newcustomer, name='new_customer'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),

]
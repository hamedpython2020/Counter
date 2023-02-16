from django.contrib import admin

# Register your models here.
from accounts.models import customer, employee, payment

admin.site.register(customer)
admin.site.register(employee)
admin.site.register(payment)

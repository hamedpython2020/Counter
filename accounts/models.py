from django.contrib.auth.models import User
from django.db import models
from datetime import datetime,date
from django.utils import timezone



class employee(models.Model):
    class Mete:
        verbose_name = "کارمند"
        verbose_name_plural = "کارمند"

    user = models.OneToOneField(User, verbose_name="کاربر", on_delete=models.CASCADE, null=False)
    id_code = models.CharField("کدملی", null=False, blank=False, max_length=10, default=1010)
    l_name = models.CharField("نام خانوادگی", max_length=30, null=False)
    join_time = models.DateTimeField("زمان عضویت", auto_now_add=True)

    def user_directory_path(instance, filename):
        return 'user/employees/{0}_{1}'.format(instance.id_code, filename)
    picture = models.ImageField("تصویر", upload_to=user_directory_path, null=True,
                                help_text="لطفا یک عکس با  فامیل خود آپلود کنید")

    def __str__(self):
        return "employee {}".format(self.l_name)
    pass

class customer(models.Model):
    class Meta:
        verbose_name = 'سازنده یا مالک'
        verbose_name_plural = "سازنده یا مالک"
        pass
    id_code = models.CharField("کدملی", null=False, blank=False, max_length=10, default=9090)
    l_name = models.CharField("نام خانوادگی", max_length=30, null=False)
    join_time = models.DateTimeField("زمان عضویت", auto_now_add=True)

    def user_directory_path(instance, filename):
        return 'user/customers/{0}_{1}'.format(instance.id_code, filename)
    picture = models.ImageField("تصویر", upload_to=user_directory_path, null=True,
                                help_text="لطفا یک عکس با  فامیل خود آپلود کنید")

    bill = models.IntegerField("صورت حساب", default=0, null=False)
    def __str__(self):
        return "customer {}".format(self.l_name)
    pass


class payment(models.Model):
    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت'
        pass
    manager = models.ForeignKey('customer', verbose_name="مسئول", on_delete=models.PROTECT, null=False)
    value = models.IntegerField('مبلغ', null=False, default=0)
    date = models.DateField("تاریخ", null=False, default=timezone.now)
    def __str__(self):
        return "{} pay {}".format(self.manager, self.value)
    pass





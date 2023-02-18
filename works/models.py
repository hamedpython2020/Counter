from django.db import models
from django.utils import timezone
from accounts.models import customer
from datetime import datetime, date

class project(models.Model):
    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه'

    code_p = models.CharField("کد نوسازی", null=False, default='0-0-0-0-0', max_length=50)
    code_erg = models.CharField("کد ارجاع", null=False, default='0', max_length=50)
    add_time = models.DateTimeField('زمان ثبت', auto_now_add=True)
    construction = 7
    land = 8
    project_finish = 9
    loading_beam = 6
    columnarization = 5
    Destruction = 1
    Foundation_concreting = 4
    Excavation = 2
    foundation = 3
    status_choices = (
        (1, 'تخریب'),
        (2, 'گودبرداری'),
        (3, 'چینش فندانسیون'),
        (4, 'بتن ریزی فندانسیون'),
        (5, 'ستون ریزی'),
        (6, 'تیر ریزی'),
        (7, 'درحال ساخت'),
        (8, 'زمین خالی'),
        (9, 'متفرقه')
    )
    status = models.IntegerField('وضعیت پروژه', choices=status_choices)
    description = models.TextField(verbose_name="توضیحات", blank=True)
    manager = models.OneToOneField(customer, on_delete=models.CASCADE, verbose_name="مالک یا سازنده")
    
    def __str__(self):
        return "{} for {}".format(self.code_p, self.manager)
    pass

class p_document(models.Model):
    class Meta:
        verbose_name = "اسناد پروژه"
        verbose_name_plural = "اسناد پروژه"
        pass
    code = models.ForeignKey('project', verbose_name="پروژه", null=False, on_delete=models.CASCADE)
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'document/{0}'.format(instance.code, filename)

    file = models.FileField(verbose_name="اسناد", help_text="لطفا تمام فایل های خود را یک جا آپلود کنید", upload_to=user_directory_path)

    def __str__(self):
        return "document for {}".format(self.code)
    pass


class Services(models.Model):
    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'
    a_p = 1
    a_fw = 2
    a_tr = 3
    a_ta = 4
    dr_plan = 5
    another = 6
    services_choices = (
        (1, 'درخواست پروانه'),
        (2, 'درخواست پایانکار'),
        (3, 'درخواست انتقال'),
        (4, 'درخواست تفکیکی'),
        (5, 'طراحی پلان'),
        (6, 'متفرقه')
    )
    define_services = models.IntegerField("خدمات تعریف شده", choices=services_choices)
    cost_services = models.IntegerField('هزینه', null=False)
    description = models.TextField("خدمات متفرقه", blank=True)
    project = models.ForeignKey("project", verbose_name="پروژه", null=False, on_delete=models.PROTECT)
    date = models.DateField("تاریخ درخواست", default=timezone.now, null=False)
    manager = models.OneToOneField(customer, verbose_name="سازنده یا مالک", null=False, on_delete=models.PROTECT)

    def __str__(self):
        return "{} for {}".format(self.define_services, self.manager)
    pass
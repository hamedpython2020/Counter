# Generated by Django 4.1.7 on 2023-02-15 19:53

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(default=1010, max_length=10, verbose_name='کدملی')),
                ('l_name', models.CharField(max_length=30, verbose_name='نام خانوادگی')),
                ('join_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان عضویت')),
                ('picture', models.ImageField(help_text='لطفا یک عکس با  فامیل خود آپلود کنید', null=True, upload_to=accounts.models.employee.user_directory_path, verbose_name='تصویر')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(default=9090, max_length=10, verbose_name='کدملی')),
                ('l_name', models.CharField(max_length=30, verbose_name='نام خانوادگی')),
                ('join_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان عضویت')),
                ('picture', models.ImageField(help_text='لطفا یک عکس با  فامیل خود آپلود کنید', null=True, upload_to=accounts.models.customer.user_directory_path, verbose_name='تصویر')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سازنده یا مالک',
                'verbose_name_plural': 'سازنده یا مالک',
            },
        ),
    ]

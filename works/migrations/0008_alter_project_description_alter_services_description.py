# Generated by Django 4.1.7 on 2023-02-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0007_alter_services_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, verbose_name='خدمات متفرقه'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-02 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20181102_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetail',
            name='phone_no',
            field=models.CharField(help_text='if your company has more than one phone number, separate them with a comma', max_length=500, verbose_name='Phone Number'),
        ),
    ]

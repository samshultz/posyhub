# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-02 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetail',
            name='email',
            field=models.CharField(blank=True, help_text='If your company has more than one email separate them by a comma', max_length=500, verbose_name='Email Addresses'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-02 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name="Company's Name")),
                ('phone_no', models.CharField(max_length=500, verbose_name='Phone Number')),
                ('email', models.CharField(help_text='If your company has more than one email separate them by a comma', max_length=500, verbose_name='Email Addresses')),
            ],
        ),
    ]

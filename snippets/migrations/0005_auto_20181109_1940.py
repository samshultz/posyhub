# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20181109_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supportemail',
            name='parent',
        ),
        migrations.AlterModelOptions(
            name='socialmedialinks',
            options={'verbose_name_plural': 'social media links'},
        ),
        migrations.DeleteModel(
            name='SupportEmail',
        ),
        migrations.DeleteModel(
            name='SupportEmails',
        ),
    ]

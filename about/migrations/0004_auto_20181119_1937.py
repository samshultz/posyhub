# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-19 18:37
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20181105_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcompany',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]

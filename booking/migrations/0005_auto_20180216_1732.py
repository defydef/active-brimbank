# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-16 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20180201_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=6),
        ),
    ]

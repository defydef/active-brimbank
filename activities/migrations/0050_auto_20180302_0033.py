# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-01 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0049_auto_20180302_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitydraft',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='activitydraft',
            name='organiser',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

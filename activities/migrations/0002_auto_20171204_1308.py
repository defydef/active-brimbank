# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 02:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='time_zone',
        ),
        migrations.AddField(
            model_name='activity',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='activity',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.TimeField(),
        ),
    ]

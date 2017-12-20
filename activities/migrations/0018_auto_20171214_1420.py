# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0017_activitydraft_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitydraft',
            name='activity_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activitydraft',
            name='activity_day',
            field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=50),
        ),
    ]
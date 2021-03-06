# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0024_auto_20171215_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(blank=True, choices=[('Sports', 'Sports'), ('Fun', 'Fun'), ('Learn', 'Learn'), ('Job', 'Get a job'), ('Culture', 'Culture')], default='Sports', max_length=100),
        ),
        migrations.AddField(
            model_name='activitydraft',
            name='activity_type',
            field=models.CharField(blank=True, choices=[('Sports', 'Sports'), ('Fun', 'Fun'), ('Learn', 'Learn'), ('Job', 'Get a job'), ('Culture', 'Culture')], default='Sports', max_length=100),
        ),
    ]

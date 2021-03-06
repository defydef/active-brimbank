# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 01:20
from __future__ import unicode_literals

import activities.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0015_activitydraft'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='flyer',
            field=models.FileField(blank=True, upload_to=activities.models.file_directory_path),
        ),
        migrations.AddField(
            model_name='activity',
            name='organiser',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='activitydraft',
            name='flyer',
            field=models.FileField(blank=True, upload_to=activities.models.file_directory_path),
        ),
        migrations.AddField(
            model_name='activitydraft',
            name='organiser',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='activitydraft',
            name='description',
            field=models.TextField(blank=True, max_length=150),
        ),
    ]

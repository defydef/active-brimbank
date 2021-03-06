# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 01:52
from __future__ import unicode_literals

import activities.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0011_activity_activity_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='created_time',
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_img',
            field=models.ImageField(blank=True, upload_to=activities.models.image_directory_path),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]

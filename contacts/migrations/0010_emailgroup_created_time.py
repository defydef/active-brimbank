# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-15 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20180104_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailgroup',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-28 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0037_auto_20180109_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='space_choice',
            field=models.CharField(choices=[('Unlimited', 'Unlimited'), ('Limited', 'Limited')], default='Unlimited', max_length=50),
        ),
        migrations.AlterField(
            model_name='activitydraft',
            name='space_choice',
            field=models.CharField(choices=[('Unlimited', 'Unlimited'), ('Limited', 'Limited')], default='Unlimited', max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendsms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendsms',
            name='message',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendsms', '0002_sendsms_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendsms',
            name='message',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-01 13:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0046_auto_20180223_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='bookmarked',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='bookmarked_users',
        ),
    ]
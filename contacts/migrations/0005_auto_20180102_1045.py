# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-01 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20180102_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smsmember',
            name='group',
        ),
        migrations.AddField(
            model_name='smsmember',
            name='group',
            field=models.ManyToManyField(null=True, related_name='sms_members', to='contacts.ContactGroup'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-21 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0017_auto_20180221_1954'),
        ('sendsms', '0018_auto_20180221_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendsms',
            name='recipient_group',
        ),
        migrations.AddField(
            model_name='sendsms',
            name='recipient_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_sms', to='contacts.ContactGroup'),
        ),
    ]
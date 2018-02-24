# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-21 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sendsms', '0015_sendemail_recipient_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendsms',
            name='recipient_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_sms', to='contacts.EmailGroup'),
        ),
    ]
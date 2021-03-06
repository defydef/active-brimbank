# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-04 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_emailgroup_emailmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmember',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email_members', to='contacts.EmailGroup'),
        ),
    ]

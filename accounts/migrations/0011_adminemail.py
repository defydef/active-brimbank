# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-01 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_modifyvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='admin', max_length=100)),
                ('email', models.EmailField(blank=True, default='devys@brimbank.vic.gov.au', max_length=254)),
            ],
        ),
    ]

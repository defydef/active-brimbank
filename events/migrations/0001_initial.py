# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=4000, null=True)),
                ('organizer', models.CharField(max_length=255, null=True)),
                ('building', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('postcode', models.CharField(max_length=4, null=True)),
            ],
        ),
    ]

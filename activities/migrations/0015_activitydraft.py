# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 09:38
from __future__ import unicode_literals

import activities.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0014_auto_20171206_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityDraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(blank=True, max_length=150)),
                ('contact_number', models.CharField(blank=True, max_length=15)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('start_time', models.TimeField(blank=True, default=datetime.datetime.now)),
                ('end_time', models.TimeField(blank=True, default=datetime.datetime.now)),
                ('activity_img', models.ImageField(blank=True, upload_to=activities.models.image_directory_path)),
                ('activity_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_drafts', to='activities.ActivityType')),
            ],
        ),
    ]

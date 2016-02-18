# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_individualhelpoffer_individual_helper'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributionevent',
            name='event_name',
            field=models.CharField(default='Distribution Event', max_length=45),
        ),
        migrations.AlterField(
            model_name='individualhelpoffer',
            name='park_and_serve_end_time',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='individualhelpoffer',
            name='park_and_serve_start_time',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
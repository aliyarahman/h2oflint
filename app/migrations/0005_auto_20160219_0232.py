# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160219_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualhelpoffer',
            name='doing_park_and_serve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='individualhelpoffer',
            name='park_and_serve_items',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='individualhelpoffer',
            name='park_and_serve_weekday',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='individualhelpoffer',
            name='will_do_admin',
            field=models.BooleanField(default=False),
        ),
    ]
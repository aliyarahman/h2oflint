# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160301_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualhelpoffer',
            name='action_needed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='individualhelpoffer',
            name='calltime_notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='individualhelpoffer',
            name='left_message',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='individualhelpoffer',
            name='no_contact',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='individualhelpoffer',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]

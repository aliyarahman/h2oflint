# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 04:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160219_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryrequest',
            name='on_behalf',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_deliveryrequest_on_behalf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='email',
            new_name='public_email',
        ),
    ]

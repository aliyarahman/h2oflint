# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160219_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualhelpoffer',
            name='will_do_plumbing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='individualhelpoffer',
            name='will_do_testing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='has_plumbing_skills',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='has_testing_skills',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='individualhelpoffer',
            name='park_and_serve_city',
            field=models.CharField(default='Flint', max_length=45),
        ),
        migrations.AlterField(
            model_name='individualhelpoffer',
            name='park_and_serve_state',
            field=models.CharField(default='MI', max_length=4),
        ),
    ]

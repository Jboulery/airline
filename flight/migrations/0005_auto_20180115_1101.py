# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_auto_20180113_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.FloatField(default=100),
        ),
    ]

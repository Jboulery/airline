# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 22:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0005_auto_20180115_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 22, 49, 25, 968331)),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_booking_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-13 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_employee_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.FileField(default='anonymous.png', upload_to=''),
        ),
    ]

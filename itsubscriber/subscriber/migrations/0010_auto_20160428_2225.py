# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import subscriber.models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0009_auto_20160428_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='archivo',
            field=models.FileField(null=True, upload_to=subscriber.models.file_name),
        ),
    ]

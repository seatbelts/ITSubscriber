# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 08:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0014_auto_20160503_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='proyecto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='subscriber.Proyecto'),
        ),
    ]

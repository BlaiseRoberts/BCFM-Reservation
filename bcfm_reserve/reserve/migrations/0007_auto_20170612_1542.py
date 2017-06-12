# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0006_auto_20170612_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_type',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reserve.ReservationType'),
            preserve_default=False,
        ),
    ]

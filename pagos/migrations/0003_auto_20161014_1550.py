# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0002_auto_20161014_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='cvv2',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='expire_month',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='expire_year',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='number',
        ),
        migrations.AddField(
            model_name='donation',
            name='payment_ref',
            field=models.CharField(default=' ', max_length=225),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0004_auto_20161014_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtype',
            name='alias',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cardtype',
            name='card_type',
            field=models.SlugField(max_length=25),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-24 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0008_auto_20170106_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160421_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
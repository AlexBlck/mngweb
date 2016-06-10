# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fm_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('data_set', models.CharField(max_length=20)),
            ],
        ),
    ]

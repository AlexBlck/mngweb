# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqcategorypage',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]

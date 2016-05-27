# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='navigationmenuitem',
            name='css_class',
            field=models.CharField(blank=True, default='', help_text='Optional styling', max_length=255, verbose_name='CSS Class'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='navigationmenuitem',
            name='menu_title',
            field=models.CharField(blank=True, default='', help_text='Optional link title in this menu                                   (defaults to page title if one exists)', max_length=255),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-09-09 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150601_1513'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Step',
            new_name='Text',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_works'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]

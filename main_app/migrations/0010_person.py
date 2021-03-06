# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_works'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('logo', models.CharField(max_length=64)),
                ('logo_alt', models.CharField(max_length=32)),
                ('birth_day', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
    ]

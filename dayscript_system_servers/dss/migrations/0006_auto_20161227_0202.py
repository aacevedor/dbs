# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-27 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0005_auto_20161227_0200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dss_server_os',
            options={'verbose_name': 'Server operative system', 'verbose_name_plural': 'Servers operatives systems'},
        ),
    ]

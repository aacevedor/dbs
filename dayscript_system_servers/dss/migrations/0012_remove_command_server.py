# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-25 00:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0011_command_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='server',
        ),
    ]

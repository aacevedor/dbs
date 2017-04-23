# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-27 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0009_auto_20161227_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='dss_server_action',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'id')),
                ('added', models.DateTimeField(auto_now=True, verbose_name=b'updated')),
                ('accion', models.CharField(max_length=500, verbose_name=b'accion')),
            ],
            options={
                'verbose_name': 'Server history',
                'verbose_name_plural': 'Servers History',
            },
        ),
    ]

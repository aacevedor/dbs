# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-27 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0012_auto_20161227_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='dss_command_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'id')),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('description', models.CharField(max_length=200, verbose_name=b'description')),
                ('added', models.DateTimeField(auto_now=True, verbose_name=b'added')),
                ('update', models.DateTimeField(auto_now=True, verbose_name=b'update')),
            ],
            options={
                'verbose_name': ' Command Type',
                'verbose_name_plural': ' Command Types',
            },
        ),
        migrations.AddField(
            model_name='dss_command',
            name='id_server_os',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='dss.dss_server_os'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dss_command',
            name='status',
            field=models.CharField(choices=[(b'0', 'Inactive'), (b'1', 'Active')], default=b'u', max_length=1, verbose_name=b'status'),
        ),
        migrations.AddField(
            model_name='dss_command',
            name='id_command_type',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='dss.dss_command_type'),
            preserve_default=False,
        ),
    ]

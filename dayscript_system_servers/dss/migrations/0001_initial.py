# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'id')),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('description', models.CharField(max_length=200, verbose_name=b'description')),
                ('command', models.CharField(max_length=200, verbose_name=b'command')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name=b'added')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated')),
                ('status', models.CharField(choices=[(b'0', 'Inactive'), (b'1', 'Active')], default=b'u', max_length=1, verbose_name=b'status')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('description', models.CharField(max_length=200, verbose_name=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'id')),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('ipv4_address', models.GenericIPAddressField(blank=True, null=True, unpack_ipv4=True, verbose_name=b'IP v4 address')),
                ('ipv6_address', models.GenericIPAddressField(blank=True, default=None, null=True, protocol=b'IPv6', unique=True, verbose_name=b'IP v6 address')),
                ('port', models.IntegerField(default=22, verbose_name=b'port')),
                ('root', models.CharField(max_length=200, verbose_name=b'root')),
                ('mac_address', models.CharField(blank=True, default=None, max_length=17, null=True, unique=True, verbose_name=b'mac_address')),
                ('description', models.CharField(max_length=200, verbose_name=b'description')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name=b'added')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated')),
                ('status', models.CharField(choices=[(b'0', 'Inactive'), (b'1', 'Active')], default=b'1', max_length=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dss.Group')),
            ],
        ),
    ]
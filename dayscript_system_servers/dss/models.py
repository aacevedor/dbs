import datetime
from django.utils import timezone
#from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .choices_options import * #import the arrays with information for input selects

class Server_group(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=200)
    description = models.CharField('description',max_length=200)
    def __str__(self):
        return unicode(self.name) or u''
    def get_id(self):
        return unicode(self.id) or u''

class Server(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=200)
    group = models.ForeignKey(Server_group,on_delete=models.CASCADE)
    ipv4_address = models.GenericIPAddressField('IP v4 address', unpack_ipv4=True, blank=True, null=True)
    ipv6_address = models.GenericIPAddressField('IP v6 address',protocol='IPv6', blank=True, null=True, unique=True, default=None)
    password = models.CharField('password',max_length=200)
    port = models.IntegerField('port',default=22)
    root = models.CharField('root',max_length=200)
    mac_address = models.CharField('mac_address',max_length=17, blank=True, null=True, unique=True, default=None)
    description = models.CharField('description',max_length=200)
    added = models.DateTimeField('added',auto_now_add=True,)
    updated = models.DateTimeField('updated',auto_now=True)
    status = models.CharField( max_length=1, choices=INTERFACE_STATUS, default='1')

    def __unicode__(self):
        return unicode(self.name) or u''

    def was_published_recently(self):
        return self.added >= timezone.now() - datetime.timedelta(days=1)

class Command(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=200)
    group = models.CharField('status', max_length=1, choices=GROUP_COMMANDS, default='u')
    description = models.CharField('description',max_length=200)
    command = models.CharField('command',max_length=200)
    added = models.DateTimeField('added',auto_now_add=True,)
    updated = models.DateTimeField('updated',auto_now=True)
    status = models.CharField('status', max_length=1, choices=INTERFACE_STATUS, default='u')


    def __str__(self):
        return self.name

class Server_history(models.Model):
    id = models.AutoField('id',primary_key=True)
    server = models.ForeignKey(Server,on_delete=models.CASCADE)
    description = models.CharField('description',max_length=200)
    command = models.CharField('command',max_length=200)
    added = models.DateTimeField('added',auto_now_add=True,)
    status = models.CharField('status', max_length=1, choices=HISTORY_STATUS, default='u')

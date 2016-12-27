import datetime
from django.utils import timezone
#from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .choices_options import * #import the arrays with information for input selects
from django.utils.translation import ugettext as t

class dss_server_group(models.Model):

    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=200)
    description = models.CharField('description',max_length=200)
    def __str__(self):
        return unicode(self.name) or u''
    def get_id(self):
        return unicode(self.id) or u''
    class Meta:
        verbose_name = t("Server Group")
        verbose_name_plural = t("Servers Groups")

class dss_server_os(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=200, choices=OPERATIVE_SYSTEM)
    version = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.CharField( max_length=1, choices=INTERFACE_STATUS, default='1')
    updated = models.DateTimeField('updated',auto_now=True)
    def __str__(self):
        return unicode(self.name) or u''
    def get_id(self):
        return unicode(self.id) or u''

    class Meta:
        verbose_name = t("Server operative system")
        verbose_name_plural = t("Servers operatives systems")


class dss_server(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=200)
    #os = models.CharField(max_length=1, choices=OPERATIVE_SYSTEM,default='0')
    id_server_os = models.ForeignKey(dss_server_os,on_delete=models.CASCADE)
    id_server_group = models.ForeignKey(dss_server_group,on_delete=models.CASCADE)
    ipv4_address = models.GenericIPAddressField('IP v4 address', unpack_ipv4=True, blank=True, null=True)
    ipv6_address = models.GenericIPAddressField('IP v6 address',protocol='IPv6', blank=True, null=True, unique=True, default=None)
    password = models.CharField('password',max_length=200)
    sshport = models.IntegerField('port',default=22)
    user = models.CharField('root',max_length=200)
    mac_address = models.CharField('mac_address',max_length=17, blank=True, null=True, unique=True, default=None)
    description = models.CharField('description',max_length=200)
    added = models.DateTimeField('added',auto_now_add=True,)
    updated = models.DateTimeField('updated',auto_now=True)
    status = models.CharField('status',max_length=1, choices=INTERFACE_STATUS, default='1')
    ram = models.DecimalField('memory ram',max_digits=3, decimal_places=2)
    dd_capacity = models.DecimalField('disc capacity',max_digits=6, decimal_places=2)
    cpu = models.CharField('cpu',max_length=200)
    def __unicode__(self):
        return unicode(self.name) or u''

    def was_published_recently(self):
        return self.added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = t(" Server")
        verbose_name_plural = t(" Servers")


class dss_server_action(models.Model):
    id = models.AutoField('id',primary_key=True)
    accion = models.CharField('accion',max_length = 500)
    id_server =  models.ForeignKey(dss_server,on_delete=models.CASCADE)
    added = models.DateTimeField('updated',auto_now=True)
    def __str__(self):
        return unicode(self.name) or u''
    def get_id(self):
        return unicode(self.id) or u''

    class Meta:
        verbose_name = t("Server action")
        verbose_name_plural = t("Servers actions")

class dss_server_history(models.Model):
    id = models.AutoField('id',primary_key=True)
    server = models.ForeignKey(dss_server,on_delete=models.CASCADE)
    description = models.CharField('description',max_length=200)
    command = models.CharField('command',max_length=200)
    added = models.DateTimeField('added',auto_now_add=True,)
    status = models.CharField('status', max_length=1, choices=HISTORY_STATUS, default='u')

    class Meta:
        verbose_name = t(" Server History")
        verbose_name_plural = t(" Servers History")

class dss_service(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=200)
    #group = models.CharField('status', max_length=1, choices=GROUP_COMMANDS, default='u')
    description = models.CharField('description',max_length=200)
    version = models.DecimalField(max_digits=4, decimal_places=2)
    added = models.DateTimeField('added',auto_now_add=True,)
    updated = models.DateTimeField('updated',auto_now=True)
    status = models.CharField('status', max_length=1, choices=INTERFACE_STATUS, default='u')


    def __str__(self):
        return self.name
    def get_id(self):
        return unicode(self.id) or u''

    class Meta:
        verbose_name = t(" Service")
        verbose_name_plural = t(" Services")

class dss_command_type(models.Model):
    id = models.AutoField('id',primary_key = True)
    name = models.CharField('name',max_length = 200)
    description = models.CharField('description', max_length = 200)
    added = models.DateTimeField('added',auto_now=True)
    update = models.DateTimeField('update',auto_now=True)
    def __str__(self):
        return unicode(self.name) or u''
    def get_id(self):
        return unicode(self.id) or u''

    class Meta:
        verbose_name = t(" Command Type")
        verbose_name_plural = t(" Command Types")

class dss_command(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=200)
    #group = models.CharField('status', max_length=1, choices=GROUP_COMMANDS, default='u')
    description = models.CharField('description',max_length=200)
    command = models.CharField('command',max_length=200)
    added = models.DateTimeField('added',auto_now_add=True,)
    updated = models.DateTimeField('updated',auto_now=True)
    status = models.CharField('status', max_length=1, choices=INTERFACE_STATUS, default='u')
    id_server_os = models.ForeignKey(dss_server_os,on_delete=models.CASCADE)
    id_command_type = models.ForeignKey(dss_command_type,on_delete=models.CASCADE)
    id_service = models.ForeignKey(dss_service,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_id(self):
        return unicode(self.id) or u''

    class Meta:
        verbose_name = t(" Command")
        verbose_name_plural = t(" Commands")

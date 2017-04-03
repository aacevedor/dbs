import datetime
import requests
import json

from django.utils import timezone
#from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .choices_options import * #import the arrays with information for input selects
from django.utils.translation import ugettext as t


# Create your models here.


class account(models.Model): 
	id = models.AutoField('id',primary_key=True)
	name = models.CharField('name',max_length = 200)
	url_api = models.CharField('url api',max_length = 200)
	token = models.CharField('token',max_length = 200)
	
	def __str__(self):
		return unicode(self.name) or u''
	def __unicode__(self):
		return unicode(self.name) or u''

	def get_id(self):
		return unicode(self.id) or u''
	class Meta:
		verbose_name = t("Ionic Account")
		verbose_name_plural = t("Ionic Accounts")



class nofication_push(models.Model):
	id = models.AutoField('id',primary_key=True)
	id_account = models.ForeignKey(account,on_delete=models.CASCADE,default='')
	sentTo = models.CharField('send to',max_length = 200)
	message = models.CharField('message',max_length = 200)
	androidmessage = models.CharField('android message',max_length = 200)
	priority = models.CharField('priority',max_length=1, choices=INTERFACE_PRIORITY, default='1')
	title = models.CharField('title',max_length = 200)
	
	def __str__(self):
		return unicode(self.name) or u''

	def __unicode__(self):
		return unicode(self.name) or u''

	def send(self):
		headers = {
		'Authorization':'Bearer %s' % self.id_account.token,
		'Content-Type':'application/json'
		}
		payload = {
		'send_to_all':self.sent_to,
		'profile':'myafarmobile',
		'notification':{
			'payload':{},
			'query':{},
			'message':self.message,
			'andorid':self.androidmessage,
			'priority':self.priority,
			'title':self.title
			}
		}
		response = requests.post(self.id_account.url,data=json.dumps(payload),headers=headers)

	class Meta:
		verbose_name = t("Ionic Notification")
		verbose_name_plural = t("Ionic Notifications")





from __future__ import unicode_literals
import os

from importlib import import_module

from django.core.exceptions import AppRegistryNotReady, ImproperlyConfigured
from django.utils._os import upath
from django.utils.module_loading import module_has_submodule
from django.apps import AppConfig


MODELS_MODULE_NAME = 'DssConfig'


class IonicConfig(AppConfig):
    name = 'ionic'
    label = "ionic"
    module = "ionic"
    url = 'ionic'
    verbose_name = 'ionic'

    def __init__(self,app_name, app_module):
    	self.name = app_name
    	self.module = app_module
    	self.label = app_name.rpartition(".")[2]
    	self.path = self._path_from_module(app_module)

	def ionicInfo(self):
		self.url = "https://api.ionic.io/push/notifications"
		print self.url
		return self

from __future__ import unicode_literals
import os

from importlib import import_module

from django.core.exceptions import AppRegistryNotReady, ImproperlyConfigured
from django.utils._os import upath
from django.utils.module_loading import module_has_submodule
from django.apps import AppConfig


MODELS_MODULE_NAME = 'DssConfig'

class DssConfig(AppConfig):
	name = "dss"
	label = "dss"
	module = "dss"
	url = 'dss'
	verbose_name = 'dss'

	def __init__(self,app_name, app_module):
		self.name = app_name
		self.module = app_module
		self.label = app_name.rpartition(".")[2]
		self.path = self._path_from_module(app_module)
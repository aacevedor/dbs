from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# - url que pertenecen al modulo dss
urlpatterns = [
    url(r'^$', views.index, name='index'), # - Ruta para el index
    url(r'^accounts/login/$', auth_views.login,{'template_name': 'registration/login.html'}),
    url(r'^ajax_process', views.ajax_process) # - Ruta para el index
]

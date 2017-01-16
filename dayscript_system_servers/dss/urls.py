from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# - url que pertenecen al modulo dss
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^record_pyro_obj/(?P<ip>.+)/(?P<pyro_obj>.+)', views.record_pyro_obj, name='record_pyro_obj'),
    url(r'^index_json/', views.index_json, name='index_json'),
    url(r'^server/(?P<server>[0-9])/service/(?P<service>.+)/command/(?P<command>.+)/show', views.server, name='command'),
    url(r'^accounts/login/$', auth_views.login,{'template_name': 'registration/login.html'}),
]

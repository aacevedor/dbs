from django.shortcuts import render, render_to_response, RequestContext,redirect
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from execute import execute
from execute import Array
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Permission

from dss.models import dss_server,dss_command,dss_server_group

from var_dump import var_dump


from dss.apps import DssConfig
from .variables import *

import Pyro4
import paramiko
import os
import json
import requests
 

# login
 
@login_required(login_url='/accounts/login/')
def index(request):
    title ="Dayscript Resources Management"
    servers = dss_server.objects.filter(status=1); # Return array with servers info
    Pyro4.config.COMMTIMEOUT = 3 #  Defined timeout for connect whit client
    Pyro4.config.COMPRESSION = True

    for server in servers:
        try:
            print 'Conectando con ' + server.ipv4_address
            info_server = Pyro4.Proxy('PYRO:'+server.pyro_object_url+'@'+ server.ipv4_address +':3000')
            info = info_server.mysqldump('asd')
            server.send_nofify_success()
            print info
        except Exception:
            print('Pyro traceback:')
            print("".join(Pyro4.util.getPyroTraceback()))
            server.send_nofify_error()
            pass
    return render(request,'index.html',{'title':title},content_type="text/html")


def record_pyro_obj(request,ip,pyro_obj):
    s = dss_server.objects.get(ipv4_address=ip)
    s.pyro_object_url = pyro_obj
    s.save()
    print s.pyro_object_url
    return HttpResponse(json.dumps('Registro Exitoso'), content_type="application/json")

def ionic(request):
    headers = {
        'Authorization': "Bearer %s" % token,
        'Content-Type': "application/json",
    }

    payload = {
                'send_to_all': 'true',
                'profile': 'myafarmobile',
                'notification': {
                    'payload': { },
                    'query':{},
                    'message': 'prueba python!',
                    'android': {
                        'message': 'Hello Android',
                        'priority': 'high',
                        'title': "Test Push"
                    }
                }
            }

    response = requests.post(ionic['url'], data=json.dumps(payload), headers=headers)


    return HttpResponse(response.text, content_type="application/json")

def ionic_push_get(request):
    payload = ''
    headers = {
        'Authorization': "Bearer %s" % token,
        'Content-Type': "application/json",
    }

    response = requests.get(url, data=payload, headers=headers)


    #url = "https://api.ionic.io//push/notifications/66770a4e-3974-46d9-bf34-81555738c76d/messages"
    #response = requests.get(url, data=payload, headers=headers)

    return HttpResponse(response.text, content_type="application/json")


def send_notify_ionic(SendTo,message,AndroidMessage,priority,title):

    headers = {
        'Authorization': "Bearer %s" % token,
        'Content-Type': "application/json",
    }
    payload = {
                'send_to_all': SendTo,
                'profile': 'myafarmobile',
                'notification': {
                    'payload': { },
                    'query':{},
                    'message': message,
                    'android': {
                        'message': AndroidMessage,
                        'priority': priority,
                        'title': title
                    }
                }
            }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return

@login_required(login_url='/accounts/login/')
def index_json(request):
    user = request.user
    if user.id:
        serverUser = dict()
        results = Array()
        g = request.user.groups.all()
        con = 0
        for index in g:
            gu = Server_group.objects.get(name=index)
            server = Server.objects.filter(group = gu.id)
            for s in server:
                result = execute('null','initial',Server.objects.get(name = s))
                result.prepare_command()
                result.excute_command()
                results[con]['nombre'] = result.dataConection.name
                results[con]['ip'] = result.dataConection.ipv4_address
                results[con]['response'] = result.dataConection.response
                results[con]['id'] = s.id
                con = con + 1
        return HttpResponse(json.dumps(results), content_type="application/json")
    return HttpResponseForbidden()

def server(request,server,service,command):
    title = 'Dayscript Resources Management'
    subtitle = 'Select option'
    output = Array()
    print command
    if server:
        subtitle = 'Select options'
        s = Server.objects.get(id=server)
        output['id'] = s.id
        output['name'] = s.name
        output['ipv4_address'] = s.ipv4_address

    if service != "all":
        subtitle = service
        output['service'] = service
        n = 0
        if service == 'files':
            n = 1
        if service == 'history':
            n = 2
        c = Command.objects.filter(group = n).values('id','command','name')
        output['commands'] = c

    if command != "all":
        subtitle = 'Execute Command'
        cq = Command.objects.get(id=command)
        sq = Server.objects.get(id = server)
        conexion = paramiko.Transport((sq.ipv4_address, sq.port))
        conexion.connect(username = sq.root, password = sq.password)
        canal = conexion.open_session()
        canal.exec_command(cq.command)
        output['execute'] = canal.makefile('rb', -1).readlines()
        conexion.close()

    return render(request,'server.html',{'title':title,'subtitle':subtitle,'data':output},content_type="text/html")

def cmd(request,service,id,command):
    results = Array()
    server = Server.objects.get(id = id)
    result = execute(service,command,Server.objects.get(name = server))
    result.prepare_command()
    result.excute_command()
    results = result.dataConection.response

    return HttpResponse(json.dumps(results), content_type="application/json")


class AllowAllKeys(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

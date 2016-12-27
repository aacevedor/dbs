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

import paramiko
import os
import json

# login

@login_required(login_url='/accounts/login/')
def index(request):
    title ="Dayscript Resources Management"
    return render(request,'index.html',{'title':title},content_type="text/html")

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

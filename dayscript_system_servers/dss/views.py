from django.shortcuts import render, render_to_response, RequestContext,redirect
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from execute import execute
from execute import Array
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Permission
from dss.models import Server,Command,Server_group

import paramiko
import os
import json

# Muestra el index de la aplicacion
@login_required( login_url='/accounts/login/' )
def index(request):
    title ="Dayscript Resources Management"
    return render(request,'index.html',{'title':title},content_type="text/html")


# controla todos los procesos ajax
@login_required()
def ajax_process( request ):
    
    return HttpResponse(json.dumps({'asd':'asd'}), content_type="application/json")


class AllowAllKeys(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

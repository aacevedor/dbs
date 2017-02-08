from django.shortcuts import render, render_to_response, RequestContext,redirect
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import JsonResponse

from execute import execute
from execute import Array
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Permission
from dss.models import dss_server,dss_command,dss_server_group

from var_dump import var_dump

import Pyro4
import paramiko
import os
import json
import requests
import pprint


@login_required(login_url='/accounts/login/')
def server_list(request,accion):
    UserLogin = request.user
    print UserLogin
    var_dump(UserLogin.is_superuser)
    return JsonResponse({'title':'lista'})

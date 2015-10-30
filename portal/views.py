# coding=utf8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.conf import settings
import json
import requests
import logging
from plugin import *
import datetime
from django.core.cache import cache
from functools import wraps
import sys
import re
import math
reload(sys)
sys.setdefaultencoding('UTF-8')

# Create your views here.
logger = logging.getLogger(__name__)
appid = "wx45d8a90044cea4f9"
secret = "ab37980a5587fd5610ccf0189a9f1253"

def wxconfig(request):
    url = request.POST['url']
    js_ticket = cache.get('js_ticket')
    s = sign(js_ticket,url)
    if request.GET.get('debug'):
        json = {
            "debug":True,
            "appId":appid,
            "timestamp":s['timestamp'],
            "nonceStr":'nameLR9969',
            "signature":s['hash'],
            "jsApiList":['onMenuShareAppMessage','onMenuShareTimeline','scanQRCode']
        }
    else :
        json = {
            "appId":appid,
            "timestamp":s['timestamp'],
            "nonceStr":'nameLR9969',
            "signature":s['hash'],
            "jsApiList":['onMenuShareAppMessage','onMenuShareTimeline','scanQRCode']
        }
    return JsonResponse(json)

def update_access_token(request):
    get_js_ticket(get_access_token(appid,secret),appid,secret)
    return JsonResponse({
        "status":"success"
    })

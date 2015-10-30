# coding=utf8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.conf import settings
import json
import requests
import logging
from models import *
import datetime
from django.core.cache import cache
from functools import wraps
import sys
import re
import math
import time
import xlwt
reload(sys)
sys.setdefaultencoding('UTF-8')

def export(request):
    taskid = request.GET.get("id")
    u = User.objects.all()
    fname = "data/data.xls"
    file = xlwt.Workbook()
    table = file.add_sheet('active',cell_overwrite_ok=True)
    table.write(0,0,'id')
    table.write(0,1,u'姓名')
    table.write(0,2,u'性别')
    table.write(0,3,u'年龄')
    table.write(0,4,u'身份证号')
    table.write(0,5,u'电话号码')
    table.write(0,6,u'创建时间')
    table.write(0,7,u'邮箱')
    line = 1
    for i in u:
        table.write(line,0,i.id)
        table.write(line,1,i.name)
        table.write(line,2,i.sex)
        table.write(line,3,i.age)
        table.write(line,4,i.card)
        table.write(line,5,i.phone)
        table.write(line,6,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(i.dateline))))
        table.write(line,7,i.email)
        line += 1
    file.save(fname)
    return HttpResponseRedirect('/data/data.xls')

def submit(request):
    name = request.POST.get("name")
    mobile = request.POST.get("mobile")
    desc = request.POST.get("desc")
    f = request.FILES['file']
    path = "data/"
    if not os.path.exists(path):
        os.mkdirs(path)
        ext = str(i).split(".")[-1]
        ext = ext.lower()
        path = 'data/' + request.POST.get("mobile") + "." + ext
        des = open(,'wb+')
        for j in i.chunks():
            des.write(j)
        des.close()
    dateline = time.time()
    u = User.objects.filter(mobile=mobile).count()
    if not u:
        user = User(name=name,mobile=mobile,desc=desc,avatar=path)
        user.save()
        return JsonResponse({
            "status":"success"    
        })
    else :
        return JsonResponse({
            "status":"fail",
            "reason":"您已经参加过了哦"
        })

from django.shortcuts import render
from django.http import HttpResponse

from .cj import caiji
from .models import SSQModel, SSQTJSimpleModel
import json


# Create your views here.

def index(request):
    details = SSQModel.objects.order_by("-serialNo").values("balls", )[:10]
    datas = []
    for it in details.iterator():
        datas.append(it['balls'].split(' '))
    resp = {'count': len(datas), 'datas': datas, 'total': SSQModel.objects.count()}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def collector(request):
    caiji.caiji()
    caiji.storage()
    return HttpResponse("处理完成")


def tjdefault(request):
    return tj(request)


def tj(request, serialno=None):
    if not serialno or not serialno.isdigit():
        details = SSQTJSimpleModel.objects.order_by("-serialNo")[:1]
    else:
        details = SSQTJSimpleModel.objects.filter(serialNo=int(serialno)).order_by("-serialNo")[:1]
    it = details[0]
    data = {"pubdate": it.pub_date}
    for num in range(1, 34):
        redball = "red%02d" % num
        exec("data['%s'] = it.%s" % (redball, redball))
    for num in range(1, 17):
        blueball = "blue%02d" % num
        exec("data['%s'] = it.%s" % (blueball, blueball))
    return HttpResponse(json.dumps(data), content_type="application/json")

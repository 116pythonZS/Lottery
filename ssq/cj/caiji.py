import requests
import json

from ..models import SSQModel, SSQTJSimpleModel

import xlrd

# r = requests.get('http://f.apiplus.net/ssq-20.json')
"""
当期数据
"""
"""
历史数据
中彩网 http://www.zhcw.com/kj/qg/ssq/wqcx/
API: http://kaijiang.zhcw.com/lishishuju/jsp/download.jsp?czId=1&czNum=5000&beginIssue=2018001&endIssue=&pageNum=1&czName=双色球
http://kaijiang.zhcw.com/lishishuju/jsp/download.jsp?czId=1&czNum=null&beginIssue=2003001&endIssue=2003160&pageNum=1&czName=%E5%8F%8C%E8%89%B2%E7%90%83
参数列表:
czId: 开始Id
czNum: 数据滆湖
beginIssue: 起始期号
endIssue: 结束期号
pageNum: 页码
czName: 彩票名称 (双色球)
"""

cp = {
    "ssq": "双色球"
}

file_name = "./双色球.xls"


def caiji():
    param = {"czId": 1, "czName": cp["ssq"]}
    obj = SSQModel.objects.last()
    if obj.serialNo:
        year = obj.serialNo // 1000
        issue = obj.serialNo % 1000
        param["beginIssue"] = obj.serialNo
        param["endIssue"] = (year+1)*1000 + issue
    else:
        param["czNum"] = 5000

    # param = {"czId": 1, "czNum": 5000, "beginIssue": "1", "endIssue": "2018300", "pageNum": 1, "czName": cp["ssq"]}
    # param = {"czId": 1, "czNum": 5000, "czName": cp["ssq"]}
    url_path = "http://kaijiang.zhcw.com/lishishuju/jsp/download.jsp"

    r = requests.get(url_path, params=param, stream=True)
    f = open(file_name, "wb")
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)


def storage():
    db = xlrd.open_workbook(file_name)
    tables = db.sheet_by_index(0)
    datas = []
    for index in range(3, tables.nrows):
        data = tables.row_values(index)
        model = SSQModel()
        model.serialNo = int(data[2])
        model.pub_date = data[1]
        model.balls = data[3]
        model.origin = ','.join(data[1:])
        datas.append(model)
    datas.sort()
    for index in range(0, len(datas)):
        tj_uncatch(datas[index])
        SSQModel.objects.get_or_create(serialNo=datas[index].serialNo)
        datas[index].save(force_update=True, update_fields=["pub_date", "balls", "origin"])


# 号码未开奖次数统计
def tj_uncatch(data):
    current, _ = SSQTJSimpleModel.objects.get_or_create(serialNo=data.serialNo)
    current.pub_date = data.pub_date
    current.balls = data.balls
    last_obj = SSQTJSimpleModel.objects.filter(serialNo__lt=data.serialNo).last()
    balls = [int(item) for item in data.balls.split(" ")]
    update_fields = ['pub_date', 'balls']
    for i in range(1, 34):
        text = "current.red%02d = not last_obj and int(1) or last_obj.red%02d + int(1)" % (i, i)
        update_fields.append("red%02d" % i)
        exec(text)
        if i < 17:
            text = "current.blue%02d = not last_obj and int(1) or last_obj.blue%02d + int(1)" % (i, i)
            update_fields.append("blue%02d" % i)
        exec(text)

    for index in range(len(balls)):
        text = "current.red%02d = int(0)" % balls[index]
        if index == (len(balls) - 1):
            text = "current.blue%02d = int(0)" % balls[index]
        exec(text)
    current.save(force_update=True, update_fields=update_fields)

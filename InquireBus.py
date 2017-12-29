#-*-coding:utf-8-*-
from requests import get
import BusException
import json
headers = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Host":"webapi.amap.com",
    "Referer":"http://www.zhbuswx.com/busline/BusQuery.html?v=2.01",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
}

#url = "http://www.zhbuswx.com/Handlers/BusQuery.ashx?handlerName=GetBusListOnRoad&lineName=K3&fromStation=拱北口岸总站"
url = "http://www.zhbuswx.com/Handlers/BusQuery.ashx"
def getResponse(url,parameters):
    response = get(url=url,params=parameters,headers =headers).text
    jsonData= json.loads(response)
    if jsonData == None or jsonData =="":
        raise BusException("网页响应结果为空")
    if jsonData["flag"] != 1002:
        raise BusException("网页响应结果有误")
    return jsonData["data"]
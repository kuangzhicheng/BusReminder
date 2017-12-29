#-*-coding:utf-8-*-
from requests import get
from BusException import BusExecption
from json import loads,load
import smtplib
from email.mime.text import MIMEText
from email.header import Header


headers = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Host":"webapi.amap.com",
    "Referer":"http://www.zhbuswx.com/busline/BusQuery.html?v=2.01",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
}
url = "http://www.zhbuswx.com/Handlers/BusQuery.ashx"
def getResponse(url,parameters):
    response = get(url=url,params=parameters,headers =headers).text
    jsonData= loads(response)
    if jsonData == None or jsonData =="":
        raise BusExecption("网页响应结果为空")
    if jsonData["flag"] != 1002:
        raise BusExecption("网页响应结果有误")
    return jsonData["data"]

def getJsonData(filepath):
    with open(filepath, "r+", encoding="utf-8") as file:
        return load(file)

def sendEmail(fromUser,toUser,message,title="公交提醒"):
    Msg = MIMEText(message)
    Msg["From"] = Header(fromUser,"utf-8")
    Msg["To"] = Header(toUser,"utf-8")
    Msg["Subject"] = Header(title,"utf-8")
    usrname ="2817902026@qq.com"
    password = "rlolplxydizsdcei"
    smtObj = None
    try:
        smtObj = smtplib.SMTP_SSL(host="smtp.qq.com",port=465)
        smtObj.login(user=usrname,password=password)
        respone = smtObj.sendmail(from_addr=fromUser,to_addrs=toUser,msg=Msg.as_string())
    except smtplib.SMTPException as e:
        print("发送邮件失败:%s"%e)
        return -1
    finally:
        if  not smtObj == None:
            smtObj.close()
    return respone





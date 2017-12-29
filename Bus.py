#-*-coding:utf-8-*-
from CommonApi import getResponse,url
import BusException
from  json import dump
from os.path import exists
from os import mkdir
class Bus(object):
    def __init__(self,line,fromStation,):
        self.name = line+'_'+fromStation
        self.line = line
        self.fromStation = fromStation
        self.id = self.getBusLineId()
    def getBusLineId(self):
        parameters = {"handlerName": "GetLineListByLineName", "key": self.line}
        try:
            respone = getResponse(url=url, parameters=parameters)
            for index in respone:
                if index["FromStation"] == self.fromStation:
                    return index["Id"]
        except BusException as e :
            print("getBusLineId():%s"%e)
            return -1
    def getBusCurrentLocation(self):
        parameters = {"handlerName": "GetBusListOnRoad", "lineName": self.line,"fromStation":self.fromStation}
        try:
            respone = getResponse(url=url, parameters=parameters)
        except BusException as e:
            print("getBusCurrentLocation():%s" % e)
            return -1
        currents = []
        for current in respone:
            currents.append(current["CurrentStation"])
        return currents

    def writeBusStationToFile(self):
        parameters = {"handlerName": "GetStationList", "lineId": self.id}
        respone = getResponse(url=url,parameters=parameters)
        path = ".\\data\\"
        if not exists(path):
            try:
                mkdir(path)
            except NotImplementedError as e:
                print("创建文件夹失败:%s"%e)
                return -1
        with open(path+"%s"%self.name+".txt",'w') as file:
            dump(respone,file,ensure_ascii=False,indent=5)
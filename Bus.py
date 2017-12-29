#-*-coding:utf-8-*-
from InquireBus import getResponse,url
import BusException
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
    def getBusCurrentLocation(self):
        parameters = {"handlerName": "GetBusListOnRoad", "lineName": self.line,"fromStation":self.fromStation}
        respone = getResponse(url=url, parameters=parameters)
        currents = []
        for current in respone:
            currents.append(current["CurrentStation"])
        return currents
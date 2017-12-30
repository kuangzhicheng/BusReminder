#-*-coding:utf-8-*-
from Bus import Bus
from CommonApi import getJsonData
from Config import listenStation
from Config import number
'''
    listenBus:监听BUS
    :return BUS对像列表
'''
def creatBusLsit(listenBus):
    busPool = []
    for line, fromStations in listenBus.items():
        for fromStation in fromStations:
            bus = Bus(line=line, fromStation=fromStation)
            busPool.append(bus)
    return busPool

'''
    busPool:BUS对像列表
'''
def updateBusStation(busPool):
    if busPool==None:
        return -1
    for bus in busPool:
        if not bus.writeBusStationToFile():
            return -1
    return 1

def NoticeUser(bus,listenStation):
   currents = bus.getBusCurrentLocation()
   busStationList = getJsonData(".\\data\\%s.txt"%bus.name)
   station = listenStation[bus.line]
   listentStationIndex= busStationList.index(station)
   for current in currents:
       currentIndex = busStationList.index(current)
       if currentIndex <= listentStationIndex:
           Temp = listentStationIndex - currentIndex
           if Temp <= number:
               message = "当前站点：%s,距离:%s,还有%s站"%(current,station,Temp)
               print(message)






if __name__ == "__main__":
    bus = Bus("603", "吉大总站")
    NoticeUser(bus,listenStation)

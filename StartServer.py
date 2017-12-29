#-*-coding:utf-8-*-
from CommonApi import getJsonData,getResponse
from Bus import Bus
import Config
if __name__ == "__main__":
    listenBus = Config.listenBus
    busPool = []
    for line,fromStations in listenBus.items():
        for fromStation in fromStations:
            bus = Bus(line=line,fromStation=fromStation)
            busPool.append(bus)


    print(busPool)

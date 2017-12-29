#-*-coding:utf-8-*-
class BusExecption(Exception):
    def __init__(self,err):
        super(BusExecption,self).__init__(err)

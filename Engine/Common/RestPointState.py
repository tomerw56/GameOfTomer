
from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point
from Engine.Common.Facade.RestPointStateFacade import RestPointStateFacade
class RestPointState(RestPointStateFacade):
    def __init__(self,position:Point):
        RestPointStateFacade.__init__(self,position)

    @RestPointStateFacade.timetoregenerate.setter
    def timetoregenerate(self, value):
        self._TimeToRegenerate = value


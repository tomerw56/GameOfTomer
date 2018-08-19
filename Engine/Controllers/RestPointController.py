from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point
from Engine.Common.RestPointState import RestPointState
from Engine.Controllers.ControllersEnums import PlayerRestPointState
from typing import List
class RestPointController:
    def __init__(self,restPointsLocations:List[Point],configprovider:ConfigProvider):
        self._ConfigProvider=configprovider;
        self._RestPointTimeToProfit = int(self._ConfigProvider.getValue("RestPoint.Config", "RestPointTimeToProfit"))
        self._RestPointTimeToRegenerate = int(
            self._ConfigProvider.getValue("RestPoint.Config", "RestPointTimeToRegenerate"))

        self._RestPoints = []
        for restpointlocation in restPointsLocations:
            self._RestPoints.append(RestPointState(restpointlocation))

    def UpdateRestingPointStateAccordingToPosition(self, position: Point, restPointTime)->PlayerRestPointState:
        for restpoint in self._RestPoints:
            restpoint.timetoregenerate = max(0, restpoint.timetoregenerate - 1)
            if restpoint.position == position:
                if restpoint.timetoregenerate == 0 and self._RestPointTimeToProfit <= restPointTime:
                    restpoint.timetoregenerate = self._RestPointTimeToRegenerate
                    return PlayerRestPointState.IN_REST_POINT_WITH_REWARD
                else:
                    return PlayerRestPointState.IN_REST_POINT_NO_REWARD
        return PlayerRestPointState.NOT_IN_RESTPOINT

    @property
    def restpoints(self):
        return self._RestPoints
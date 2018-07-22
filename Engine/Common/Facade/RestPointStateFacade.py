from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point


class RestPointStateFacade():
    def __init__(self, position: Point):
        self._Position = position
        self._TimeToRegenerate = 0

    @property
    def position(self):
        return self._Position

    @property
    def timetoregenerate(self):
        return self._TimeToRegenerate
    def __str__(self):
        return ' Position={0} TimeToRegenerate={1}'.format(self._Position, self._TimeToRegenerate)

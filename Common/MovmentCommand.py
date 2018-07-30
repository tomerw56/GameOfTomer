from Common.Point import Point
class MovementCommand:
    def __init__(self,pFrom,pTo):
        self._From=pFrom
        self._To=pTo
    @property
    def pointFrom(self):
        return self._From
    @property
    def pointTo(self):
        return self._To
    @staticmethod
    def GetEmpty():
        return MovementCommand(Point.GetEmpty(),Point.GetEmpty())

    def __str__(self):
        return 'from={0} To= {1}'.format(self._From,self._To)
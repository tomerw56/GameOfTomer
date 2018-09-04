from Common.Point import Point
class MovementCommand:
    def __init__(self,pTo:Point=Point(-1,-1)):

        self._To=pTo
    @property
    def pointTo(self):
        return self._To

    @property
    def IsEmpty(self):
        return self._To.IsEmpty
    @staticmethod
    def GetEmpty():
        return MovementCommand(Point(-1,-1))

    def __str__(self):
        return 'from={0} To= {1}'.format(self._To)
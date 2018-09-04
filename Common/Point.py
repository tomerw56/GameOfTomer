class Point:
    def __init__(self,x,y):
        self._X=x
        self._Y=y


    @property
    def x(self):
        return self._X

    @property
    def y(self):
        return self._Y


    @x.setter
    def x(self, value):
        self._X = value

    @y.setter
    def y(self, value):
        self._Y = value

    @staticmethod
    def ToGridNode(x,y,rownumber):
        return x + (y * rownumber)

    @staticmethod
    def ToGridNodeFromPoint(point, rownumber):
        return point.x + (point.y * rownumber)

    @staticmethod
    def GetEmpty():
        return Point(-1,-1)

    @property
    def IsEmpty(self):
        return self._Y==-1 and self._X==-1

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.x == other.x
            and self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return 'X={0} Y= {1}'.format(self._X,self._Y)
from Common.Point import Point
class Dimensions:
    def __init__(self,width,height):
        self._Width=width
        self._Height=height


    @property
    def width(self):
        return self._Width

    @property
    def height(self):
        return self._Height

    @width.setter
    def width(self, value):
        self._Width = value

    @height.setter
    def height(self, value):
        self._Height = value

    def IsPointInDim(self, point:Point):
        if point.x>=self.width:
            return False
        if point.y>=self.height:
            return False
        if point.y<0:
            return False
        if point.x<0:
            return False
        return True
    def __str__(self):
        return 'Width={0} Height= {1}'.format(self._Width,self._Height)

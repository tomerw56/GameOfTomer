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

    def getString(self):
        return 'Width={0} Height= {1}'.format(self._Width,self._Height)

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

    @property
    def x(self):
        return self._X

    @x.setter
    def x(self, value):
        self._X = value

    @y.setter
    def y(self, value):
        self._Y = value
    def __str__(self):
        return 'X={0} Y= {1}'.format(self._X,self._Y)
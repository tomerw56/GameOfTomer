class PathResult:
    def __init__(self,points:list,valid:bool=False,nodelist=[]):
        self._Points=points
        self._Nodelist=nodelist
        self._Valid=valid
    @property
    def points(self):
        return self._Points

    @property
    def valid(self):
        return self._Valid

    @property
    def nodelist(self):
        return self._Nodelist

    @points.setter
    def points(self, value):
        self._Points = value



    @nodelist.setter
    def nodelist(self, value):
        self._Nodelist = value

    @valid.setter
    def valid(self, value):
        self._Valid = value
    def __str__(self):
        return 'Valid={0} points= {1}'.format(self._Valid,self._Points)
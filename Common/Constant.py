class Constants:
    def __init__(self):
        self._CoverNumber=100
        self._MaximumAltDif=2
        self._ConnectedGraphVertexWeight=1
        self._UnConnectedGraphVertexWeight = 100

    @property
    def CoverNumber(self):
        return self._CoverNumber

    @property
    def MaximumAltDif(self):
        return self._MaximumAltDif
    @property
    def ConnectedGraphVertexWeight(self):
        return self._ConnectedGraphVertexWeight
    @property
    def UnConnectedGraphVertexWeight(self):
        return self._UnConnectedGraphVertexWeight

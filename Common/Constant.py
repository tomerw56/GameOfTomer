class Constants:
    def __init__(self):
        self._CoverNumber=100
        self._MaximumAltDif=2
        self._ConnectedGraphVertexWeight=1
        self._InValidAlt = -1
        self._UnConnectedGraphVertexWeight = 100
        self._ReordFileNameTemplate="Step_{0}.json"
        self._RecordGameMetaDataFileName="GameMetaData.json"
        self._MovementGraphFileName = "MovementGraph.json"
        self._ControllingPointsFileName = "ControllingPoints.json"


    @property
    def CoverNumber(self):
        return self._CoverNumber

    @property
    def RecordGameMetaDataFileName(self):
        return self._RecordGameMetaDataFileName

    @property
    def ControllingPointsFileName(self):
        return self._ControllingPointsFileName

    @property
    def MovementGraphFileName(self):
        return self._MovementGraphFileName

    @property
    def ReordFileNameTemplate(self):
        return self._ReordFileNameTemplate

    @property
    def MaximumAltDif(self):
        return self._MaximumAltDif
    @property
    def ConnectedGraphVertexWeight(self):
        return self._ConnectedGraphVertexWeight
    @property
    def UnConnectedGraphVertexWeight(self):
        return self._UnConnectedGraphVertexWeight
    @property
    def InValidAlt(self):
        return self._InValidAlt
class Constants:
    def __init__(self):
        self._MaximumAltDif=2
        self._SafePointValue = 99
        self._ConnectedGraphVertexWeight=1
        self._InValidAlt = -1
        self._UnConnectedGraphVertexWeight = 100
        self._SaftypointCloseRange=2
        self._ThreatTimeTillPunisment = 2
        self._ReordFileNameTemplate="Step_{0}.json"
        self._RecordGameMetaDataFileName="GameMetaData.json"
        self._MovementGraphFileName = "MovementGraph.json"
        self._ControllingPointsFileName = "ControllingPoints.json"
        self._SafePointsFileName = "SafePoints.json"



    @property
    def RecordGameMetaDataFileName(self):
        return self._RecordGameMetaDataFileName

    @property
    def ThreatTimeTillPunishment(self):
        return self._ThreatTimeTillPunisment


    @property
    def SafetypointCloseRange(self):
        return self._SaftypointCloseRange

    @property
    def ControllingPointsFileName(self):
        return self._ControllingPointsFileName

    @property
    def SafePointsFileName(self):
        return self._SafePointsFileName

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
    @property
    def SafePointValue(self):
        return self._SafePointValue
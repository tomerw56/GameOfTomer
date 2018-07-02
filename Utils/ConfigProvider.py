class ConfigProvider:

    def __init__(self):
        self._ConfigValid=False
        pass

    def getValue(self,key,subkey):
        pass
    @property
    def ConfigValid(self):
        return self._ConfigValid

    @ConfigValid.setter
    def ConfigValid(self, value):
        self._ConfigValid = value
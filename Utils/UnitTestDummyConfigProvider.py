from Utils.ConfigProvider import ConfigProvider
import configparser

class UnitTestDummyConfigProvider(ConfigProvider):
    def __init__(self):
        ConfigProvider.__init__(self)
        self._config = configparser.ConfigParser()
        self.ConfigValid=True
    def addValue(self,key,subkey,val):
        self._config[key] = {}
        self._config[key][subkey]=val

    def setValue(self, key, subkey, val):

        self._config[key][subkey] = val

    def getValue(self, key, subkey):
        return self._config[key][subkey]

    @property
    def ConfigValid(self):
        return super(UnitTestDummyConfigProvider, self).ConfigValid

    @ConfigValid.setter
    def ConfigValid(self, value):
        self._ConfigValid = value
        super(UnitTestDummyConfigProvider, self.__class__).ConfigValid.fset(self, value)





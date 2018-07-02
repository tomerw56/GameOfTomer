import os

from Utils.ConfigProvider import ConfigProvider
import configparser


class IniConfigProvider(ConfigProvider):
    def __init__(self, configfilename):
        ConfigProvider.__init__(self)
        if not os.path.isfile(configfilename):
            self.ConfigValid  = False
            return
        self._config = configparser.ConfigParser()
        self._config.read(configfilename)
        self.ConfigValid = True

    def getValue(self, key, subkey):
        return self._config[key][subkey]

    @property
    def ConfigValid(self):
        return super(IniConfigProvider, self).ConfigValid

    @ConfigValid.setter
    def ConfigValid(self, value):
        self._ConfigValid = value
        super(IniConfigProvider, self.__class__).ConfigValid.fset(self, value)
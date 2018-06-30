import os.path
import numpy as np
import pickle

class MapHolder:
    def __init__(self,mapname):
        self.Mapname=mapname
        self.MapLoaded=self.LoadMap(mapname)

    def LoadMap(self,mapname):
        if os.path.isfile(mapname):
            self.Map = pickle.load(open(self.Mapname, "rb"))
        else:
            self.Map=np.asmatrix(np.zeros((10,10)))
        return True
    def SaveMap(self,mapname):
        if self.MapLoaded:
            pickle.dump(self.Map, open(self.Mapname, "wb"))

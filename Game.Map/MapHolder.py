import os.path
import numpy as np
import pickle
import collections

class MapHolder:
    def __init__(self,mapname):

    def LoadMap(self,mapname):
        if os.path.isfile(mapname):
            self.Map = pickle.load(open(self.Mapname, "rb"))
        else:
            self.Map=np.asmatrix(np.ones((10,10)))
        self.Mapname = mapname
        self.MapLoaded = True
        return self.MapLoaded
    def SaveMap(self,mapname):
        if self.MapLoaded:
            pickle.dump(self.Map, open(self.Mapname, "wb"))
    def  getMapDim(self):
        Dimensions = collections.namedtuple('Dimensions', ['width', 'height'])
        dim=Dimensions(width=0,height=0)
        if self.MapLoaded:
            dim.width,dim.height=self.Map.shape



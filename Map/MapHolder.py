import os.path
import numpy as np
import pickle
from Common.Dimensions import Dimensions
from Common.Constant import Constants
import networkx as nx

from Map.CSVMatrixReader import CSVMatrixReader


class MapHolder:
    def __init__(self):
        self._GraphLoaded = False
        self._Consts=Constants()
        self._Csvreader = CSVMatrixReader()

    def loadMap(self,mapname):
        self._Csvreader.parse(mapname)
        if  self._Csvreader.fileLoaded:
            self.buildGraph()
        else:
            self._Map=np.asmatrix(np.ones((10,10)))
        self._Mapname = mapname
        return  self._Csvreader.fileLoaded
    def saveMap(self,mapname):
        pass
    def getMapDim(self):
        dim=Dimensions(0,0)
        if  self._Csvreader.fileLoaded:
            dim.width,dim.height=self._Csvreader.Matrix.shape
        return dim

    def mayMove(self,p1,p2):
        if not  self._Csvreader.fileLoaded:
            return False
        return True


    def buildGraph(self):
        dim=self.getMapDim()
        numberOfNodes=(dim.width*dim.height)-1

        self._Graph = nx.Graph()
        for i in range(0, numberOfNodes):
           self._Graph.add_node(i)
        for colIndex in range(0, dim.width):
            for rowIndex in range(0, dim.height):
                cord = self.getConnectivtyNodeIndex(colIndex, rowIndex, dim.height)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,0)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,1)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,-1)

                self.UpdateWeight(cord,colIndex,rowIndex,dim,-1,0)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,-1,1)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, -1,-1)

                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1,0)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1, -1)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1, 1)
        self._GraphLoaded=True
    def UpdateWeight(self,cord,colIndex,rowIndex,dim,xFactor,yFactor):
        newColIndex=colIndex+xFactor
        newRowIndex=rowIndex+yFactor

        if (newColIndex)>dim.width:
            return
        if (newColIndex)<0:
            return
        if (newRowIndex)>dim.height:
            return
        if (newRowIndex)<0:
            return
        #we try to go to Cover -not connected
        NextCord=self.getConnectivtyNodeIndex(newColIndex,newRowIndex,dim.height)
        if self._Csvreader.Matrix.item((colIndex, rowIndex)) == self._Consts.CoverNumber:
            self._Graph.add_weighted_edges_from((NextCord, cord, self._Consts.UnConnectedGraphVertexWeight))
            return
        # we try to go from Cover -not connected

        if self._Csvreader.Matrix.item((newColIndex, newRowIndex)) == self._Consts.CoverNumber:
            self._Graph.add_weighted_edges_from((NextCord,cord,self._Consts.UnConnectedGraphVertexWeight))
            return

        # Alt Diff Issue
        AltDiff=abs(self._Csvreader.Matrix.item((colIndex, rowIndex))-self._Csvreader.Matrix.item((newColIndex, newRowIndex)))
        if AltDiff >= self._Consts.MaximumAltDif:
            self._Graph.add_weighted_edges_from((NextCord, cord, self._Consts.UnConnectedGraphVertexWeight))
            return
        #we set connectivity
        self._Graph.add_weighted_edges_from((NextCord, cord, self._Consts.ConnectedGraphVertexWeight))
    def getConnectivtyNodeIndex(self,x,y,rownumber):
        return x+(y*rownumber)
    @property
    def map(self):
        return self._Csvreader.Matrix
    @property
    def mapLoaded(self):
        return  self._Csvreader.fileLoaded
    @property
    def graphLoaded(self):
        return self._GraphLoaded





import networkx as nx
import matplotlib.pyplot as plt
from Utils.ConfigProvider import ConfigProvider
from Common.Constant import Constants
from  Common.PathResult import PathResult
from  Common.Point import Point
class MovementCalculator:
    def __init__(self,configProvider):
        self._Consts = Constants()
        self._ConfigProvider=configProvider
    def mayMove(self,pFrom,pTo,graph):
        try:
            length=nx.shortest_path_length(graph,pFrom,pTo)
            maximumAllowedPath=self._ConfigProvider.getValue('Game.MovementDefinations','maximumAllowedPath')
            return  (int(maximumAllowedPath)>=length)
        except nx.exception.NetworkXError:
            return False
        except nx.exception.NetworkXError:
            return False
    def getPath(self,pFrom,pTo,graph):

        try:
            path = nx.shortest_path(graph,pFrom,pTo)
            NodeList=[]
            for idx in range(0,len(path)):
                point=Point(graph.nodes[path[idx]]["X"],graph.nodes[path[idx]]["Y"])
                NodeList.append(point)
            maximumAllowedPath = self._ConfigProvider.getValue('Game.MovementDefinations', 'maximumAllowedPath')

            result = PathResult(NodeList, int(maximumAllowedPath) >= len(NodeList),path)
            return result
        except nx.exception.NetworkXNoPath:
            result= PathResult([],False)
            return result
        except nx.exception.NetworkXError:
            result = PathResult([], False)
            return result


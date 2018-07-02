import networkx as nx
from Utils.ConfigProvider import ConfigProvider
from Common.Constant import Constants
class MovementCalculator:
    def __init__(self,configProvider):
        self._Consts = Constants()
        self._ConfigProvider=configProvider
    def mayMove(self,pFrom,pTo,graph):
        try:
            length=nx.shortest_path_length(graph,pFrom,pTo)
            maximumAllowedPath=self._ConfigProvider.getValue('Game.MovementDefinations','maximumAllowedPath')
            if(int(maximumAllowedPath)<length):
                return False;
            return True
        except nx.exception.NetworkXError:
            return False
    def getPath(self,pFrom,pTo,graph,draw=fale):
        try:
            path = nx.shortest_path(G, source=14, target=16)

            import matplotlib.pyplot as plt
            G = nx.karate_club_graph()
            pos = nx.spring_layout(G)
            nx.draw(G, pos, node_color='k')
            # draw path in red
            path_edges = zip(path, path[1:])
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='r')
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=10)
            plt.axis('equal')
            plt.show()

        except nx.exception.NetworkXError:
            return []


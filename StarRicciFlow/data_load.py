
import graph_generate
import os
import networkx as nx
from utils_gamma import *

class Graph:

    def __init__(self, graph, args=None, data_dir=None):
        self.graph = graph
        # we enter this first if
        if data_dir == None and args['my_graph'] == False:
            self.G = getattr(nx, graph, None)(*args['settings'])
        elif data_dir == None and args['my_graph'] == True:
                self.G = getattr(graph_generate, graph)(*args['settings'])
        else:
            self.G = nx.read_gexf("karate.gexf") # change this to work for any graph
        
        n_edges = len(self.G.edges())
        weight = {e: 1.0 for e in self.G.edges()}
        nx.set_edge_attributes(self.G, weight, 'weight')
        self.node_colors()
        DrawGraphWithEdgeLength(self.G, "before.svg")
        print("Data loaded. \nNumber of nodes： {}\nNumber of edges: {}".format(self.G.number_of_nodes(), self.G.number_of_edges()))

    def node_colors(self):
        if self.graph == 'karate_club_graph':
            for i in self.G.nodes():
                if self.G.nodes[i]['club'] == 'Officer':
                    self.G.nodes[i]['color'] = '#377eb8'
                else:
                    self.G.nodes[i]['color'] = '#ff7f00'
        else:
            pass

if __name__ == "__main__":
    graph = Graph('karate_club_graph')
    nx.write_gexf(graph.G, "karate.gexf")


"""
Graph implementation (Seite 258)
"""


import networkx as nx
import matplotlib.pyplot as plt
from numpy import array


class Graph:
    def __init__(self):
        self.verteces = set()  # Letters
        self.edges = set()     # tuples of Letters
        
    # Knoten hinzufügen
    def add_vertex(self, vertex):
        ...
        
    # Kante hinzufügen
    def add_edge(self, edge: tuple):
        ...
        
    # Alle von einem Knoten ausgehenden Kanten ermitteln
    def edges_from_vertex(self, vertex):
        ...
        
    # Alle direkt mit einem Knoten verbindenen Nachbarn ermitteln
    def get_neighbors(self, vertex):
        ...
        
    # Kante entfernen
    def remove_edge(self, edge: tuple):
        ...
        
    # Knoten (und alle mit ihm verbundenen Kanten) entfernen
    def remove_vertex(self, vertex):
        ...
    
    def __str__(self):
        return ""
    
    def to_adjacency_matrix(self):
        verteces = sorted(self.verteces)
        n = len(verteces)
        mx = list(); [mx.append([0]*n) for _ in range(n)]  # initialize mx with zeros
        d = {v:i for i,v in enumerate(verteces)}
        for (f,t) in self.edges:
            mx[d[f]][d[t]] = 1
        return mx
            
    def draw(self):
        G = nx.from_numpy_matrix(array(self.to_adjacency_matrix()))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=False)
        nx.draw_networkx_labels(G, pos, labels={i:v for i,v in enumerate(sorted(self.verteces))})
        plt.show()






graph = Graph()
graph.verteces = {'A', 'B', 'C', 'D'}
graph.edges = {('A', 'B'), ('B', 'A'), ('A', 'C'), ('C', 'A')}

mx = graph.to_adjacency_matrix()
print(*mx, sep='\n')


graph.draw()









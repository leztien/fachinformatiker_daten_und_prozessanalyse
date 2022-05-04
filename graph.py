
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
        self.costs = dict()
        
    # Knoten hinzufügen
    def add_vertex(self, vertex):
        self.verteces.add(vertex)
        
    # Kante hinzufügen
    def add_edge(self, edge: tuple, cost=None):
        f,t = edge   # f = from, t = to
        self.verteces.add(f)
        self.verteces.add(t)
        self.edges.add((f,t))
        self.edges.add((t,f))
        
        # Kosten hinzufügen
        if cost:
            try:
                self.costs[(f,t)], self.costs[(t,f)]  = cost
            except TypeError:
                self.costs[(f,t)] = self.costs[(t,f)] = cost

        
    # Alle von einem Knoten ausgehenden Kanten ermitteln
    def get_edges_from_vertex(self, vertex):
        return set(filter(lambda t: t[0]==vertex, self.edges))
        
        
    # Alle direkt mit einem Knoten verbindenen Nachbarn ermitteln
    def get_neighbors(self, vertex):
        return {t[-1] for t in self.get_edges_from_vertex(vertex)}
        
    # Kante entfernen
    def remove_edge(self, edge: tuple):
        f,t = edge
        self.edges.remove((f,t))
        self.edges.remove((t,f))
        
        if (f,t) in self.costs:
            self.costs.pop((f,t))
            self.costs.pop((t,f))
        
    # Knoten (und alle mit ihm verbundenen Kanten) entfernen
    def remove_vertex(self, vertex):
        #edges = self.get_edges_from_vertex(vertex)
        for edge in self.get_edges_from_vertex(vertex):
            self.remove_edge(edge)
        self.verteces.remove(vertex)
    
    def __str__(self):
        s = ""
        for vertex in sorted(self.verteces):
            s += "{:s}: {}\n".format(vertex, sorted(self.get_neighbors(vertex)))
        return s
    
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

##########################################################################

class Node:
    def __init__(self, state, parent=None, cost=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        
    def __eq__(self, other):
        return self.state == other.state
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __hash__(self):
        return self.state
    
    def __repr__(self): return f"{self.__class__.__name__}({self.state})"
    def __str__(self):  return self.__repr__()
    
    
def dfs(start_state, is_goal, get_neighbors):
    frontier = [Node(start_state)]
    visited = {start_state}
    
    while frontier:
        node = frontier.pop()   # Stack functionality
        
        if is_goal(node.state):
            path = [node.state,]
            while node.state != start_state:
                node = node.parent
                path.append(node.state)
            return path[::-1]
        
        
        for neighbor in get_neighbors(node.state):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            frontier.append( Node(neighbor, parent=node) )

###################################################################


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edge(['A', 'B'], cost=1)
g.add_edge(['B', 'C'], cost=2)
g.add_edge(['C', 'D'], cost=0.5)
g.add_edge(['A', 'E'], cost=3)
g.add_edge(['E', 'F'], cost=0.5)
g.add_edge(['F', 'G'], cost=3)
g.add_edge(['A', 'F'], cost=3)
g.add_edge(['C', 'F'], cost=0.5)



print(g)
g.draw()


path = dfs(start_state = 'A',
           is_goal = lambda state: state == 'G',
           get_neighbors = g.get_neighbors)

print("path =", path)



# Topological Sorting
"""
Sorts given actions in such a way that if there is a dependecy of one action on another, 
then the dependent action always comes later than its parent action.
"""
# Using stack
from collections import defaultdict

class Graph:
    def __init__(self,numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def topologicalSortUtil(self, v ,visited, stack):
        visited.append(v)
        
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
                
        stack.insert(0,v)
        
    

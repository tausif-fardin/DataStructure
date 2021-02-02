#create a graph

class Graph:
    def __init__(self,gdict = None): #creating an empty dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    

customDict = { "a" : ["b","c"],
"b" : ["a","e"],
"c" : ["a","e"],
"d" : ["b","e","f"],
"e" : ["d","f","c"],
"f" : ["d","e"]
}


graph = Graph(customDict)
graph.addEdge("f","a")
print(graph.gdict)

#Depth First Search
#Using Stack

class Graph:
    def __init__(self,gdict = None): #creating an empty dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def dfs(self, vertex):  
        visitedV = [vertex]
        stack = [vertex]
        while stack: #while stack is not empty
            popVertex = stack.pop() #this will remove last element from the stack
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visitedV:
                    visitedV.append(adjacentVertex)
                    stack.append(adjacentVertex)
            
            
customDict = { "a" : ["b","c"],
              "b" : ["a","e"],
              "c" : ["a","e"],
              "d" : ["b","e","f"],
              "e" : ["d","f","c"],
              "f" : ["d","e"]
}
graph = Graph(customDict)
graph.dfs("a")
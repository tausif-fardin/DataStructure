#Breadth First Search
#Using queue data structures.

class Graph:
    def __init__(self,gdict = None): #creating an empty dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def bfs(self, vertex):
        visitedV = [vertex]
        queue = [vertex] #using list as queue

        while queue:
            deVertex = queue.pop(0) #this will remove first element from the list
            print(deVertex)
            for adjacentVertext in self.gdict[deVertex]:
                if adjacentVertext not in visitedV:
                    visitedV.append(adjacentVertext)
                    queue.append(adjacentVertext)


customDict = { "a" : ["b","c"],
              "b" : ["a","e"],
              "c" : ["a","e"],
              "d" : ["b","e","f"],
              "e" : ["d","f","c"],
              "f" : ["d","e"]
}
graph = Graph(customDict)
graph.bfs("a")
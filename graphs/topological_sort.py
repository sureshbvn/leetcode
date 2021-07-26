import collections
class Graph:
    def __init__(self,numVertices):
        self.v = numVertices
        self.adjList = {}
    
    def addEdge(self, v1, v2):
        if v1 not in self.adjList:
            self.adjList[v1] = []
        # Adding only in one direction to make sure that we are creating
        # directed graphs.
        self.adjList[v1].append(v2)
    
    def dfs(self):
        visited = {}
        
        def helper(source):
            for neighbour in self.adjList[source]:
                if neighbour not in visited:
                    print(neighbour)
                    helper(neighbour)
                
                visited[neighbour] = True

        for vertex in self.adjList:
            print("The vertex taken", vertex)
            if vertex not in visited:
                visited[vertex] = True
                print(vertex)
                helper(vertex)

g = Graph(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(4,0)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(4,1)
g.dfs()


    

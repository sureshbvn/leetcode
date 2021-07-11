import collections
def length_of_shortest_path(graph, a, b):
    def getNeighbours(node):
        # Return the adj list of the node.
        return graph[node]
    
    def bfs(root, target):
        queue = collections.deque([root])
        visited = set([root])
        level = 0
        while len(queue) > 0:
            levelLen = len(queue)
            for i in range(levelLen):
                node = queue.popleft()
                if node == target:
                    return level
                
                for neighbour in getNeighbours(node):
                    if neighbour in visited:
                        continue
                    queue.append(neighbour)
                    visited.add(neighbour)
            level = level + 1
    return bfs(a, b)

graph = {}
graph[0] = [1, 2]
graph[1] = [0, 2, 3]
graph[2] = [0, 1]
graph[3] = [1]
print(length_of_shortest_path(graph,0, 3))

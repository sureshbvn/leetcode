import collections

grid = [[1,2,3], [4,5,6], [7,8,9]]
numRows = len(grid)
numCols = len(grid[0])

def getNeighbours(coord):
    row, col = coord
    deltaRow = [-1, 0, 1, 0]
    deltaCol = [0, 1, 0, -1]
    res = []
    for i in range(len(deltaRow)):
        neigbhourRow = row + deltaRow[i]
        neighbourCol = col + deltaCol[i]
        if 0 <= neigbhourRow < numRows and 0 <= neighbourCol < numCols:
            res.append((neigbhourRow, neighbourCol))
        
    return res

def bfs(startNode):
    queue = collections.deque([startNode])
    visited = set([startNode])
    while len(queue) > 0:
        node = queue.popleft()

        print(node)
        # Note that we are not checking if node is not already visited. We cannot ignore
        # if a node is already visited, we should make sure that all the neighbours of this
        # node are visited.
        for neighbour in getNeighbours(node):
            # If neighbour is visited, this means the neigbhour is alrady in the queue.
            # So the neighbours of this neighbour are already explored or going to be
            # explored because it is in queue. We dont need to do anything.
            if neighbour in visited:
                continue
            
            # Add them to the queue. Note that we are adding for nodes that are not
            # yet visited to the queue. So the queue will not have duplicate nodes.
            queue.append(neighbour)


            # Mark the neigbhour as visited. The neigbhours of this neigbours will be
            # explored when this neighbour is popped from the queue.
            visited.add(neighbour)

bfs((0,0))

def floodFill(image, sr, sc, newColor):
        
    # Get all the neigbhours for the given cordinate.
    def getNeigbhours(coord, color):
            
        neigbhours = []
        deltaRows = [0, -1, 0, 1]
        deltaCols = [-1, 0, 1, 0]
        maxNumRows = len(image)
        maxNumCols = len(image[0])
            
        row, col = coord
        for i in range(0, len(deltaRows)):
            newRow = row + deltaRows[i]
            newCol = col + deltaCols[i]
                
            # Check if the new row and col is within the matrix range.
            if 0 <= newRow < maxNumRows and 0 <= newCol < maxNumCols:
                    
                # Now check if the neigbhour is of color. If so, include it.
                if image[newRow][newCol] == color:
                    neigbhours.append((newRow, newCol))
            
        return neigbhours
        
    def bfs(source):
        queue = collections.deque([source])
        visited = [[False for c in range(len(image[0]))] for r in range(len(image))]
        r, c = source
        color = image[r][c]
        image[r][c] = newColor
            
        while len(queue) > 0:
            numNodes = len(queue)
            for i in range(numNodes):
                node = queue.popleft()
                    
                for neigbhour in getNeigbhours(node, color):
                    r, c = neigbhour
                    if visited[r][c]:
                        continue
                        
                    queue.append((neigbhour))
                    visited[r][c] = True
                    image[r][c] = newColor
        
    bfs((sr,sc))
    return image
    
image = [[0,0,0],[0,0,0]]
print(floodFill(image, 0, 0, 2))
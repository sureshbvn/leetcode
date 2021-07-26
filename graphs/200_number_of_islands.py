class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            
        numRows = len(grid)
        numCols = len(grid[0])
            
        visited = [[0 for _ in range(0, numCols)] for _ in range(0, numRows)]
        print(visited)
            
        def dfs(xcord, ycord):
            if xcord< 0 or ycord <0:
                return 
                
            if xcord >= numRows or ycord >= numCols:
                return
                
            if grid[xcord][ycord] == "0":
                return
                
            if visited[xcord][ycord] > 0:
                return
            
            visited[xcord][ycord] = 1
            
            dfs(xcord, ycord+1)
            dfs(xcord, ycord-1)
            dfs(xcord-1, ycord)
            dfs(xcord+1, ycord)
        
        def getNeigbhours(xcord, ycord):
            
            x = [0, 0, 1, -1] 
            y = [1, -1, 0, 0]
            
            neighbours = []
            for i in range(0, len(x)):
                    newRow = xcord + x[i]
                    newCol = ycord + y[i]
                    
                    if newRow < 0 or newCol < 0:
                        continue
                    
                    if newRow >= numRows or newCol >= numCols:
                        continue
                    
                    neighbours.append((newRow, newCol))
            return neighbours
                        
                    
    
        def bfs(row, col):
            queue = collections.deque([(row, col)])
            
            while len(queue) > 0:
                node = queue.popleft()
                neighbours = getNeigbhours(node[0], node[1])
                for r, c in  neighbours:
                    if visited[r][c] == 1:
                        continue
                    
                    if grid[r][c] != "1":
                        continue
                    
                    queue.append((r,c))
                    visited[r][c] = 1
                

            
        connected = 0
        for row in range(0, numRows):
            for col in range(0, numCols):
                if visited[row][col] == 1:
                    continue 
                
                if grid[row][col] == "1":
                    bfs(row, col)
                    connected = connected + 1
            
        return connected
                        
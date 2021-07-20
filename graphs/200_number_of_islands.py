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
            
            
        connected = 0
        for row in range(0, numRows):
            for col in range(0, numCols):
                if visited[row][col] == 1:
                    continue 
                
                if grid[row][col] == "1":
                    dfs(row, col)
                    connected = connected + 1
            
        return connected
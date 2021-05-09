# We can start from any cell in the first row. 
# We can iterate either in left diognal and right diognal. 
# We can also iterate down.
def maxGoldCoins(grid):
    def helper(i, j):
        if i >= len(grid) or j>= len(grid[0]):
            return [0, 0, 0]
        
        if i < 0 or j < 0:
            return [0, 0, 0]

        if i == len(grid)-1 and j == len(grid[0])-1:
            return [grid[i][j], grid[i][j], grid[i][j]]
        
        if i == len(grid)-1 and j < len(grid[0])-1:
            return [grid[i][j], grid[i][j], grid[i][j]]

        leftd = helper(i+1, j-1)[0] + grid[i][j]
        rightd = helper(i+1, j+1)[1] + grid[i][j]
        down = helper(i+1, j)[2] + grid[i][j]

        return leftd, rightd, down 
    
    m = 0
    for j in range(0, len(grid[0])):
        output = helper(0, j)
        for coins in output:
            m = max(m, coins)
    
    return m

grid1 = [[0,1,1,0], [1,1,0,1], [1,1,0,1], [1,1,1,1]]
print("The max number of gold coins", maxGoldCoins(grid1))

grid2 = [[0,1,1], [0,1,0], [0,0,1]]
print("The max number of gold coins", maxGoldCoins(grid2))
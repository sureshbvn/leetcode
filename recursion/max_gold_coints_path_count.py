# There is a grid. In each cell there is possiblity of
# gold coin. The start at of the iteration is (0,0).
# We can either move right or go down. What is the maximum
# number of gold coins that can be collected use this.
# Return the total number of paths.
def maxGoldCoinsPaths(grid):

    def helper(i, j):

        # First row and first column.
        if i == 0 and j == 0:
            return [grid[i][j], 1]
        
        # First row second column onwards.
        if i > 0 and j == 0:
            up = helper(i-1, j)
            return [up[0]+grid[i][j], up[1]]
        
        # First column second row onwards.
        if i ==0 and j >0:
            left = helper(i, j-1)
            return [left[0]+grid[i][j], left[1]]
        
        up = helper(i-1, j)
        left = helper(i, j-1)

        if up[0] == left[0]:
            return [up[0] + grid[i][j], up[1]+left[1]]
        
        if up[0] > left[0]:
            return [up[0]+grid[i][j], up[1]]
        else:
            return [left[0]+grid[i][j], left[1]]
    
    return helper(len(grid)-1, len(grid[0])-1)

grid1 = [[0,1,1,0], [1,1,0,1], [1,1,0,1], [1,1,1,1]]
result1 = maxGoldCoinsPaths(grid1)
print("The max number of gold coins", result1[0])
print("The max number of paths", result1[1])

grid2 = [[0,1,1], [0,1,0], [0,0,1]]
result2 = maxGoldCoinsPaths(grid2)
print("The max number of gold coins", result2[0])
print("The max number of paths", result2[1])
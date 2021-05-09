# There is a grid. In each cell there is possiblity of
# gold coin. The start at of the iteration is (0,0).
# We can either move right or go down. What is the maximum
# number of gold coins that can be collected use this.
def maxGoldCoins(grid):
    def helper(i, j):
        if i < 0 and j < 0:
            return 0

        if i == 0 and j==0:
            return grid[i][j]

        if i == 0 and j >0:
            return helper(i, j-1) + grid[i][j]
        
        if i > 0 and j==0:
            return helper(i-1, j) + grid[i][j]

        return max(helper(i-1, j), helper(i, j-1)) + grid[i][j]
    return helper(len(grid)-1, len(grid[0])-1)

grid1 = [[0,1,1,0], [1,1,0,1], [1,1,0,1], [1,1,1,1]]
print("The max number of gold coins", maxGoldCoins(grid1))


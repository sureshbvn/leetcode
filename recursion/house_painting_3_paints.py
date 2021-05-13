# There are N houses in a row. We can paint them 
# using R, B, G. Painting a house with a color has 
# a cost. The cost varies by house. No two adjacent
# houses can be painted the same color. 
# What is the minimum cost to paint all the colors.

def housePainting(grid):
    cost = [0 for i in range(0, len(grid))]
    def helper(houseIndex, cost):
        if houseIndex < 0:
            return [0 for i in range(0, len(grid)+1)]
        
        if houseIndex == 0:
            return [grid[0][j] for j in range (0, len(grid[0]))]
        
        previousCost = helper(houseIndex-1, cost)
        newCost = [0 for i in range(0, len(grid)+1)]
        newCost[0] = min(previousCost[1], previousCost[2]) + grid[houseIndex][0]
        newCost[1] = min(previousCost[0], previousCost[2]) + grid[houseIndex][1]
        newCost[2] = min(previousCost[0], previousCost[1]) + grid[houseIndex][2]

        return newCost

    
    return helper(1, cost)

l = housePainting([[1,2,3], [4,5,6]])
print(l)


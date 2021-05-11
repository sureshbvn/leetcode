# There are N houses in a row. We can paint them 
# using R or B. Painting a house with R or B has 
# a cost. The cost varies by house. No two adjacent
# houses can be painted the same color. 
# What is the minimum cost to paint all the colors.

def housePainting(grid):
    def helper(houseIndex, blueCost, redCost):
        if houseIndex < 0:
            return [0,0]

        if houseIndex == 0:
            return [grid[0][0], grid[0][1]]

        # By calling this cost array will be populated till
        # houseIndex-1. 
        output = helper(houseIndex-1, blueCost,redCost)
        previousBlueCost = output[0]
        b = output[1] + grid[houseIndex][0]
        r = previousBlueCost + grid[houseIndex][1]
        return [b, r]
    l = len(grid)-1
    output = helper(l, 0, 0)
    return min(output[0], output[1])

cost = housePainting([[20,30], [15,30], [30,40], [20,30]])
print("The cost of painting ", cost)


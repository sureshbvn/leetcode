def minCostClimbingStairs(cost): 
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        def helper(i):
            if i <= 1:
                return 0
            
            return min(helper(i-1)+cost[i-1], helper(i-2)+cost[i-2])
            
        return helper(len(cost))

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
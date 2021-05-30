# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
ef minCostClimbingStairs(cost): 
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        def helper(i):
            if i <= 1:
                return 0
            
            return min(helper(i-1)+cost[i-1], helper(i-2)+cost[i-2])
            
        return helper(len(cost))

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
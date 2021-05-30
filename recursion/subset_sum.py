# Count number of subsets the will sum up to given target sum.

def subsets(subset, targetSum):
    # The helper recursive function. Instead of passing a slate(subset), we are 
    # passing the remaining sum that we are interested in. This will reduce the
    # overall complexity of problem from (2^n)*n to (2^n).
    def helper(sum, index):
        # Base condition. Only when we are at a leaf node, the subset is 
        # completely formed.
        if index == len(subset):
            # If sum reaches zero, this is equivalent to subset sum.
            # In the slate world, we will have actual subset at this stage.
            if sum == 0:
                return 1
            return 0

        if sum < 0:
            return 0
        
        return helper(sum-subset[index], index+1) + helper(sum, index+1)
    
    return helper(targetSum, 0)

count = subsets([1,2,3,4], 6)
print("The total number of subsets with target sum", count)
    
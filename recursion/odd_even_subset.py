# Find all possible subsets such that sum of the subset is equal 
# to target sum but you can only take values on even index together 
# or odd index together.

def subsets(input, targetSum):
    # The helper recursive function.
    def helper(sum, index, slate, odd):
        if index >= len(input):
            if sum == 0:
                print(slate[:])
                return 1
            return 0
        
        if odd:
            if index%2 == 0:
                slate.append(input[index])
                c1 = helper(sum-input[index], index+2, slate, odd)
                slate.pop()
                c2 = helper(sum-input[index], index+2, slate, odd)
                return c1+c2
        return 0
    
    return helper(sum, 0, [], True)

count = subsets([1,2,3,4], 5)
print("The number of subsets: %d", count)


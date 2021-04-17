# Positive integers in the array and you can take any 
# number maximum K times. You need to find the number of 
# subsets for which the sum is equal to the target sum.
def subsets(input, targetSum, k):

    def helper(sum, index, slate, count):
        # Add the base conditions later.
        if count > k:
            return 0
        
        if sum == 0:
            print(slate[:])
            return 1
        
        if sum < 0:
            return 0
        
        if index == len(input):
            return 0

        slate.append(input[index])
        #print("after appending", slate)
        c1 = helper(sum-input[index], index, slate, count+1)
        #print("before popping", slate)
        slate.pop()
        #print("after popping", slate)
        c2 = helper(sum, index+1, slate, 0)
        return c1 + c2

    return helper(targetSum, 0, [], 0)

count = subsets([1,2,3,4], 5, 5)
print("The number of subsets", count)

# Unique integers in the array and you can take any 
# number maximum K times. You need to find the number of 
# subsets for which the sum is equal to the target sum.
def subsets(input, targetSum, k):

    def helper(sum, index, slate, count):
        # Add the base conditions later.
        if count > k:
            return 0
        
        # This is the key difference between the array having only 
        # positive numbers and negative numbers also. In case of the
        # case where array has only positive numbers we can bail out
        # early if the sum reaches less than zero. This is because of the
        # fact that next number that we will possible see in the next index
        # will only be positive and will increase the sum even more. But in case
        # of negative numbers we can obtain a negative number to reduce the sum to zero.
        # So to determenstically tell, we should process the complete subset.
        if index == len(input):
            if sum == 0:
                print(slate[:])
                return 1
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

count = subsets([-1,1,2,3,4], 5, 2)
print("The number of subsets", count)

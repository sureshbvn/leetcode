# Unique positive numbers in the array and 
# you can take any number infinite times. 
# You need to find the number of subsets 
# for which the sum is equal to the target sum.
def subsets(input, targetSum):

    # Helper recursion function to find out of number of subsets 
    # that will be equal to given sum
    def helper(sum, index, slate):
        # If the sum is less than zero, there is no point going
        # towards that path, as the path will only contain
        # more postive elements.
        if sum < 0:
            return 0

        # If sum is zero, the current subset which is captured in the
        # slate corresponds to a subset that we are interested in. The
        # slate is only passed along to understand what subset is resulting
        # in interested target.
        if sum == 0:
            print(slate[:])
            return 1
        
        # If we reach the end of the array, there are no more elements to process,
        # return. This is to handle the case where a subset is properly formed and 
        # the sum of that is greater than zero.
        if index == len(input):
            return 0

        slate.append(input[index])
        c1 = helper(sum-input[index], index, slate)
        slate.pop()
        c2 = helper(sum, index+1, slate)

        return c1+c2
    
    count = helper(targetSum, 0, [])
    return count

count = subsets([1,2,3,4,5,6], 6)
print("The number of subsets", count)
def maxProfit(prices):
    def helper(index):
        # Base case. Return the last element.
        if index == len(prices)-1:
            return [0, prices[index]]
            
        # Otherwise solve the sub problem starting i+1.
        s, m = helper(index+1)
            
        newsolution = m-prices[index]
        return [max(newsolution, s), max(prices[index], m)]
        
    ans = helper(0)
    return ans[0]

print(maxProfit([7,1,5,3,6,4]))
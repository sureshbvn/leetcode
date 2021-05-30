# You are given an array prices where prices[i] 
# is the price of a given stock on the ith day.
# You want to maximize your profit by choosing 
# a single day to buy one stock and choosing a 
# different day in the future to sell that stock.
# Return the maximum profit you can achieve from this 
# transaction. If you cannot achieve any profit, return 0.
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
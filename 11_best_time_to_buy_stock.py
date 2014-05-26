#!/usr/bin/env
class Solution:
    def maxProfit(self, prices):
	max_profit = 0
	if not prices: return 0
	else:
	    for i in range(1, len(prices)):
                if (prices[i] > prices[i-1]):
		    max_profit += prices[i] - prices[i-1]
            return max_profit

so = Solution()
prices1 = [1,2]
profit1 = so.maxProfit(prices1)
assert profit1 == 1
print profit1
prices2 = [1,2,4]
profit2 = so.maxProfit(prices2)
assert profit2 == 3
print profit2

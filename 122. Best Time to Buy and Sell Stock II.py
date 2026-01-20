from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [ prices[i] - prices[i-1] for i in range(1, len(prices)) ]
        arr = [ x for x in arr if x > 0]
        
        return sum(arr)

    # def maxProfit(self, prices: List[int]) -> int:
        # result = 0
        # for i in range(1, len(prices)):
        #     diff = prices[i] - prices[i-1]
        #     if diff > 0:
        #         result += diff

        # return result
    
prices = [7,1,5,3,6,4]

sol = Solution()
ans = sol.maxProfit(prices)
print(ans)
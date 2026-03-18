#
# @lc app=leetcode id=2280 lang=python3
#
# [2280] Minimum Lines to Represent a Line Chart
#

# @lc code=start
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:        
        stockPrices.sort(key= lambda x: x[0])

        pre_dx, pre_dy = 0, 1
        ans = 0        

        for prev, cur in zip(stockPrices, stockPrices[1:]):
            x1, y1 = prev
            x2, y2 = cur
            dx, dy = x2 - x1, y2 - y1

            if dx * pre_dy != dy * pre_dx:
                ans += 1
                pre_dx, pre_dy = dx, dy
                    
        return ans
    
# @lc code=end

# stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
# stockPrices = [[3,4],[1,2],[7,8],[2,3]]
stockPrices = [[72,98],[62,27],[32,7],[71,4],[25,19],[91,30],[52,73],[10,9],[99,71],[47,22],[19,30],[80,63],[18,15],[48,17],[77,16],[46,27],[66,87],[55,84],[65,38],[30,9],[50,42],[100,60],[75,73],[98,53],[22,80],[41,61],[37,47],[95,8],[51,81],[78,79],[57,95]]

sol = Solution()
ans = sol.minimumLines(stockPrices)
print(ans)
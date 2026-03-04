#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)        
        
        while len(stones) > 1:
            

            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            
            n = y-x
            if n != 0:
                heapq.heappush_max(stones, n)
        
        return 0 if len(stones) == 0 else stones[0]
# @lc code=end

stones = [2,7,4,1,8,1]

sol = Solution()
ans = sol.lastStoneWeight(stones)
print(ans)
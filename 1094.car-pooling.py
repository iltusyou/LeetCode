#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = {}
        
        for n, from_, to in trips:
            d[from_] = d.get(from_, 0) + n
            d[to] = d.get(to, 0) - n                    

        keys = list(d.keys())
        keys.sort()

        s = 0
        for k in keys:
            s += d[k]
            if s > capacity:
                return False
        
        return True
# @lc code=end

trips = [[2,1,5],[3,3,7]]
capacity = 4

sol = Solution()
ans = sol.carPooling(trips, capacity)
print(ans)
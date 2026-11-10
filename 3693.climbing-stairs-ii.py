#
# @lc app=leetcode id=3693 lang=python3
#
# [3693] Climbing Stairs II
#

# @lc code=start
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:        

        lst = [0, costs[0] + 1]
        
        if n == 1:
            return costs[0] + 1

        cost2 = costs[1] + min(4, lst[-1] + 1)
        lst.append(cost2)

        if n == 2:
            return lst[-1]

        cost3 = costs[2] + min(9, lst[-2] + 4, lst[-1] + 1)        
        lst.append(cost3)

        if n == 3:
            return lst[-1]

        for i in range(4, n+1):
            cost = costs[i-1] + min(lst[-3] + 9, lst[-2] + 4, lst[-1] + 1)        
            lst.append(cost)        

        return lst[-1]


# @lc code=end


n = 4
costs = [1,2,3,4]

sol= Solution()
ans = sol.climbStairs(n, costs)
print(ans)

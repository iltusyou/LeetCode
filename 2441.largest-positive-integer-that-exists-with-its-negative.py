#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        res = []

        for n in nums:
            if n * -1 in s:                                
                res.append(abs(n))
            s.add(n)

        if not res:
            return -1

        return max(res)
# @lc code=end

# nums = [-1,2,-3,3]
# nums = [-1,10,6,7,-7,1]
nums = [-10,8,6,7,-2,-3]

sol = Solution()
ans = sol.findMaxK(nums)
print(ans)
#
# @lc app=leetcode id=3379 lang=python3
#
# [3379] Transformed Array
#

# @lc code=start
from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        for i in range(l):
            j = i + nums[i]

            if j >= l:
                j = j % l

            elif j < 0:
                j = j % l




            res[i] = nums[j]
            
        return res
# @lc code=end

# nums = [3,-2,1,1]
# nums = [-1,4,-1]
nums = [-10]

sol = Solution()
ans = sol.constructTransformedArray(nums)
print(ans)
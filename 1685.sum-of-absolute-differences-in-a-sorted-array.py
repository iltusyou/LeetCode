#
# @lc app=leetcode id=1685 lang=python3
#
# [1685] Sum of Absolute Differences in a Sorted Array
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = list(accumulate(nums, initial=0))
        
        ans = []

        l = len(nums)

        for i in range(l):
            left = (i+1) * nums[i] - (s[i+1])
            right = (s[-1] - s[i+1]) - ((l-i-1) * nums[i])
            ans.append(left + right)

        return ans
            

        
# @lc code=end

# nums = [2,3,5]
nums = [1,4,6,8,10]

sol = Solution()
ans = sol.getSumAbsoluteDifferences(nums)
print(ans)
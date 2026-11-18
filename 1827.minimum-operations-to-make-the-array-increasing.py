#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        ans = 0 
        for i in range(1, n):
            if nums[i] < nums[i-1]+1:
                d = nums[i-1]+1 - nums[i]
                nums[i] += d
                ans += d

        return ans
    
# @lc code=end

nums = [1,1,1]

sol = Solution()
ans = sol.minOperations(nums)
print(ans)
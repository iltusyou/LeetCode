#
# @lc app=leetcode id=3364 lang=python3
#
# [3364] Minimum Positive Sum Subarray 
#

# @lc code=start
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        nums_len = len(nums)
        d = [0] * (nums_len+1)

        prefix_sum = 0

        for i in range(nums_len):
            prefix_sum += nums[i]
            d[i+1] = prefix_sum


        res = float('inf')
        for i in range(l, r+1):
            for j in range(i, nums_len+1):
                sub_sum = d[j] - d[j-i]
                if sub_sum > 0 and sub_sum < res:
                    res = sub_sum                                
        return res
        
# @lc code=end

nums = [3, -2, 1, 4]
l = 2
r = 3

sol = Solution()
ans = sol.minimumSumSubarray(nums, l, r)
print(ans)
#
# @lc app=leetcode id=3350 lang=python3
#
# [3350] Adjacent Increasing Subarrays Detection II
#

# @lc code=start
from itertools import pairwise
from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        cur = 1
        for x, y in pairwise(nums):
            if y > x:
                cur+=1
            else: 
                arr.append(cur)
                cur = 1

        arr.append(cur)

        ans = 0
        for x, y in pairwise(arr):
            t = min(x, y)
            ans = max(ans, t)   

        ans = max(ans, max(arr)//2)       

        return ans
# @lc code=end

# nums = [2,5,7,8,9,2,3,4,3,1]
nums = [1,2,3,4,4,4,4,5,6,7]

sol = Solution()
ans = sol.maxIncreasingSubarrays(nums)
print(ans)

#
# @lc app=leetcode id=3427 lang=python3
#
# [3427] Sum of Variable Length Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        l = len(nums)
        arr = [nums[0]]
        for i in range(1, l):
            start = max(0, i - nums[i])
            
            arr.append(nums[i] + arr[-1])

            tmp = arr[i] -  arr[start]
            print(start, i, tmp)

        return arr
        
# @lc code=end

nums = [3,1,1,2]
sol = Solution()
ans = sol.subarraySum(nums)
print(ans)
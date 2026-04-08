#
# @lc app=leetcode id=3107 lang=python3
#
# [3107] Minimum Operations to Make Median of Array Equal to K
#

# @lc code=start
from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        n = len(nums)
    
        mid_i, ans = n//2, 0

        for i in range(mid_i + 1, n):            
            if nums[i] >= k:
                break

            ans += (k - nums[i])

        for i in range(mid_i - 1, -1, -1):                         
            if nums[i] <= k:
                break

            ans += (nums[i] - k)

        print(ans)

        ans += abs(nums[mid_i] - k)

        return ans
# @lc code=end

# nums = [2,5,6,8,5]
# k = 4

# nums = [2,5,6,8,5]
# k = 7

# nums = [1,2,3,4,5,6]
# k = 4

nums = [45,50,89,30,4,5,91,58]
k = 31

sol = Solution()
ans = sol.minOperationsToMakeMedianK(nums, k)
print(ans)
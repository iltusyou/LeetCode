#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#

# @lc code=start
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)
        ans = float('inf')
        for i in range(n-k+1):
            ans = min(ans, nums[i+k-1] - nums[i])            

        return ans
# @lc code=end

# nums = [90]
# k = 1

nums = [9,4,1,7]
k = 2

sol = Solution()
ans = sol.minimumDifference(nums, k)
print(ans)
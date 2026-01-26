#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
                
        dp = [0] * (len(nums)+2)
        
        for i in range(len(nums)):            
            j = i +2
            dp[j] = max(dp[j-1], dp[j-2]+nums[i])
            print(dp)
        
        return dp[-1]
        
# @lc code=end

nums = [2,7,9,3,1]
# nums = [2,1]
# nums = [1,3,1]

sol = Solution()
ans = sol.rob(nums)
print(ans)
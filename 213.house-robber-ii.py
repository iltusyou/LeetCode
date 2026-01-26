#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List


class Solution:
    def rob1(self, nums: List[int]) -> int:                        
        dp = [0] * (len(nums)+2)
        
        for i in range(len(nums)):            
            j = i +2
            dp[j] = max(dp[j-1], dp[j-2]+nums[i])
            print(dp)
        
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        n = len(nums)
        res1 = self.rob1(nums[:n-1])
        res2 = self.rob1(nums[1:])

        return max(res1, res2)
        
# @lc code=end
nums = [1,2,3,1]
sol = Solution()
ans = sol.rob(nums)
print(ans)

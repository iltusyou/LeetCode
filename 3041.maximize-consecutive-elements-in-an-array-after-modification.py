#
# @lc app=leetcode id=3041 lang=python3
#
# [3041] Maximize Consecutive Elements in an Array After Modification
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums = sorted(nums)        
        dp = defaultdict(int)
        
        for x in nums:
            if dp[x]+1 > dp[x+1]:
                dp[x+1] = dp[x] + 1

            if dp[x-1]+1 > dp[x]:
                dp[x] = dp[x-1]+1            
            
        ans = max(dp.values())
        return ans

        

            


     




          



                

        
# @lc code=end

# nums = [2,1,5,1,1]
nums = [8,10,6,12,9,12,2,3,13,19,11,18,10,16]

sol = Solution()
ans = sol.maxSelectedElements(nums)
print(ans)
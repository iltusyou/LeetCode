#
# @lc app=leetcode id=2860 lang=python3
#
# [2860] Happy Students
#

# @lc code=start
from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()
        nums.append(100001)        
        
        ans = 0 if nums[0] == 0 else 1
                
        for i in range(n):
            if nums[i] < i+1 < nums[i+1]:
                ans += 1                

        return ans
    
    
# @lc code=end

nums = [6,0,3,3,6,7,2,7]
# nums = [1,1,0,1]

sol = Solution()
ans = sol.countWays(nums)
print(ans)
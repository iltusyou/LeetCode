#
# @lc app=leetcode id=2567 lang=python3
#
# [2567] Minimum Score by Changing Two Elements
#

# @lc code=start
from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        
        nums.sort()
        
        a1 = nums[-3] - nums[0] #刪除最大兩個
        a2 = nums[-1] - nums[2] #刪除最小兩個
        a3 = nums[-2] - nums[1]  #刪除1最大1最小
        ans = min(a1, a2, a3)
     
        return ans
    
# @lc code=end

# nums = [1,4,7,8,5]
nums = [59,27,9,81,33]

sol = Solution()
ans = sol.minimizeSum(nums)
print(ans)
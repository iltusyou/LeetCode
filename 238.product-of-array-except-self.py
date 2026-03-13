#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix = [1] * n

        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i] 
            suffix[i-1] = product        

        ans = [1] * n
        product = 1        
        for i in range(n):            
            ans[i] = product * suffix[i]
            product *= nums[i]
        
        return ans
    
# @lc code=end
nums = [1,2,3,4]

sol = Solution()
ans = sol.productExceptSelf(nums)
print(ans)

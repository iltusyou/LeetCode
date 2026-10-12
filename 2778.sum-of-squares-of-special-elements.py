#
# @lc app=leetcode id=2778 lang=python3
#
# [2778] Sum of Squares of Special Elements 
#

# @lc code=start
import math
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        r = math.isqrt(n)

        sum = 0

        for i in range(r+1):
            if n % (i+1) == 0:
                sum += nums[i] * nums[i]

        if n > 1:                
            sum += nums[-1] * nums[-1]    
        
        return sum
# @lc code=end

# nums = [1,2,3,4]
nums = [2,7,1,19,18,3]

sol = Solution()
ans = sol.sumOfSquares(nums)
print(ans)
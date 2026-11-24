#
# @lc app=leetcode id=3411 lang=python3
#
# [3411] Maximum Subarray With Equal Products
#

# @lc code=start
from typing import List
import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)   

        ans = 0
        for i in range(n):
            p, g, l = nums[i], nums[i], nums[i]
            cnt = 1

            for j in range(i+1, n):
                p *= nums[j]
                if p > 2520:
                    break

                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])
                
                if p == g * l:
                    cnt = j-i+1

            ans = max(ans, cnt)

        return ans
    
# @lc code=end

nums = [1,2,1,2,1,1,1]
sol = Solution()
ans = sol.maxLength(nums)
print(ans)
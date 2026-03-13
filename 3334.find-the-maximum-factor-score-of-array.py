#
# @lc app=leetcode id=3334 lang=python3
#
# [3334] Find the Maximum Factor Score of Array
#

# @lc code=start
from math import gcd, lcm
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] * nums[0]

        suf_gcd = [0] * (n + 1)
        suf_lcm = [0] * n + [1]

        for i in range(n - 1, -1, -1):            
            suf_gcd[i] = gcd(suf_gcd[i + 1], nums[i])
            suf_lcm[i] = lcm(suf_lcm[i + 1], nums[i])

        # print(suf_gcd, suf_lcm)                                    

        ans = suf_gcd[0] * suf_lcm[0]

        pre_gcd, pre_lcm = 0, 1

        for i, x in enumerate(nums):
            tmp = gcd(pre_gcd, suf_gcd[i+1]) * lcm(pre_lcm, suf_lcm[i+1])
            ans = max(ans, tmp)

            pre_gcd = gcd(pre_gcd, x)
            pre_lcm = lcm(pre_lcm, x)
              
        return ans
    
# @lc code=end

nums = [2,4,8,16]
# nums = [1,2,3,4,5]

sol = Solution()
ans = sol.maxScore(nums)
print(ans)
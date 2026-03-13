#
# @lc app=leetcode id=1979 lang=python3
#
# [1979] Find Greatest Common Divisor of Array
#

# @lc code=start
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m, n = max(nums), min(nums)

        def gcd(a, b):
            while a!=0:
                tmp = a
                a = b%a
                b = tmp
            return b
        
        ans = gcd(m, n)

        return ans
# @lc code=end

nums = [2,5,6,9,10]
nums = [7,5,6,8,3]
nums = [3,3]

sol = Solution()
ans = sol.findGCD(nums)
print(ans)


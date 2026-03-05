#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
from cmath import sqrt
from math import isqrt


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n <= 0:
            return False                
        
        for p in [2, 3, 5]:
            while n % p ==0:
                n //= p

        return n == 1

# @lc code=end

n = -8
sol = Solution()
ans = sol.isUgly(n)
print(ans)
#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
#

# @lc code=start
from math import gcd


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        return int(n / gcd(2, n) * 2) 
    
# @lc code=end

n = 5
sol = Solution()
ans = sol.smallestEvenMultiple(n)
print(ans)

#
# @lc app=leetcode id=1447 lang=python3
#
# [1447] Simplified Fractions
#

# @lc code=start
from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(2, n+1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    ans.append(f"{j}/{i}")
                    
        return ans
# @lc code=end

n = 3

sol = Solution()
ans = sol.simplifiedFractions(n)
print(ans)
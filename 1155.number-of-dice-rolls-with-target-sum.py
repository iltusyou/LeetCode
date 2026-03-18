#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
from math import factorial


class Solution:
    def combination(self, n: int, m: int) -> int:
        return factorial(n) / (factorial(n-m) * factorial(m))

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        def cnt(n, target):
            print(n, target)
            if n == 1:
                if target <= k:
                    return 1
                return 0
            
            s = 0
            for i in range(1, k+1):
                s += cnt(n-1, target-i)
            return s
                        
        ans = cnt(n, target)
        MOD = 10_000_000_07
        ans = ans % MOD

        return ans
# @lc code=end

# n = 1 
# k = 6 
# target = 3

n = 2
k = 6
target = 7

# n = 30
# k = 30
# target = 500

sol = Solution()
# ans = sol.numRollsToTarget(n, k, target)
# print(ans)

print(sol.combination(499, 29) - sol.combination(499, 29))

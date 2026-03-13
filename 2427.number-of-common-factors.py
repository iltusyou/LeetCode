#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        p = 2
        ans = 1

        while (a >= p and b >= p):
            
            if a % p == 0 and b % p == 0:
                e = 1
                a, b = a//p, b//p
            
                while a % p == 0 and b % p == 0:
                    e += 1
                    a, b = a//p, b//p

                ans *= (e+1)

            p += 1

        return ans
# @lc code=end

# a = 12
# b = 6

a = 25
b = 30

sol = Solution()
ans = sol.commonFactors(a, b)
print(ans)
#
# @lc app=leetcode id=1925 lang=python3
#
# [1925] Count Square Sum Triples
#

# @lc code=start
from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n+1):
            for b in range(a, n+1):
                p = a*a + b*b                

                if p > n* n:
                    break

                c = sqrt(p)
                if c == int(c):
                    cnt += 2   
                    # print(a, b, c)                             

        return cnt
# @lc code=end


n = 250
sol = Solution()
ans = sol.countTriples(n)
print(ans)
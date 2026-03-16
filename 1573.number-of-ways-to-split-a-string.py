#
# @lc app=leetcode id=1573 lang=python3
#
# [1573] Number of Ways to Split a String
#

# @lc code=start
from math import factorial

class Solution:       
    def numWays(self, s: str) -> int:        
        indexs = [i for i, x in enumerate(s) if x == '1']
        cnt = len(indexs)

        if cnt % 3 != 0:
            return 0

        if cnt == 0:
            n = len(s)            
            ans = ((n-1)* (n-2)//2)
        
        else:
            p = cnt//3
            ans = (indexs[p] - indexs[p-1]) * (indexs[-p] - indexs[-1-p])                                

        MOD = 10_000_000_07
        ans = ans % MOD

        return ans
# @lc code=end

# s = "10101"
# s = "1001"
# s = "0000"
# s = "100100010100110"
s = "00000000"

sol = Solution()
ans = sol.numWays(s)
print(ans)
#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
       
        for i in range(1, len(s)):
            if s[i] == 'a' and s[i-1] == 'b':
                return False
                               
        return True
# @lc code=end

# s = "aaabbb"
# s = "abab"
s = "bbb"
s = "aaa"

sol = Solution()
ans = sol.checkString(s)
print(ans)
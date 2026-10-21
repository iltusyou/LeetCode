#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans, bal = 0, 0
        for x in s:
            if x == '(':
                bal += 1
            else:
                bal -= 1

            if bal < 0:
                ans += 1
                bal += 1

        if bal > 0:
            ans += bal
        
        return ans
# @lc code=end

s = "())"
s = "()))(("

sol = Solution()
ans = sol.minAddToMakeValid(s)
print(ans)
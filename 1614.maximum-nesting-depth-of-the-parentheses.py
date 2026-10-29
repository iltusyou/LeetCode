#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        curr = 0
        for x in s:
            if x == '(':
                curr += 1
            elif x == ')':
                curr -= 1
            else:
                ...

            if curr > ans:
                ans = curr
                            
        return ans
# @lc code=end

s = "(1+(2*3)+((8)/4))+1"

sol = Solution()
ans = sol.maxDepth(s)
print(ans)
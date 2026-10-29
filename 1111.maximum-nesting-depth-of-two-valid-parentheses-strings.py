#
# @lc app=leetcode id=1111 lang=python3
#
# [1111] Maximum Nesting Depth of Two Valid Parentheses Strings
#

# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:

        curr = 0
        ans = []
        
        for x in seq:
            if x == '(':
                curr += 1
            else:
                curr -= 1

            if (x == '(' and curr % 2 == 1) or (x==')' and curr % 2 == 0):
                ans.append(0)
            else:
                ans.append(1)

        return ans

            
            
# @lc code=end

seq = "()(())()" #[0,0,0,1,1,0,1,1]

sol = Solution()
ans = sol.maxDepthAfterSplit(seq)
print(ans)
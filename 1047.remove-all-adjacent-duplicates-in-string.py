#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stacks = []
        
        for c in s:
            if len(stacks) == 0:
                stacks.append(c)

            elif stacks[-1] == c:
                stacks.pop(-1)

            else:
                stacks.append(c)
        
        res = "".join(stacks)
        return res
    
# @lc code=end

s = "abbaca"
sol = Solution()
ans = sol.removeDuplicates(s)
print(ans)
#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        for c in s:
            if c == '(':
                stacks.append(')')        
            elif c == '[':
                stacks.append(']')
            elif c == '{':
                stacks.append('}')
            else:
                if len(stacks) == 0:
                    return False
                elif stacks[-1] != c:
                    return False
                else:
                    stacks.pop(-1)                        

        return len(stacks) == 0
# @lc code=end

s = "]"
sol = Solution()
ans = sol.isValid(s)
print(ans)


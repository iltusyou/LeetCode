#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#

# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        stacks = []
        for c in s:
            stacks.append(c)

            if len(stacks) >= 2 and ((stacks[-1]=='B' and stacks[-2] == 'A') or (stacks[-1]=='D' and stacks[-2] == 'C')):
                stacks.pop()
                stacks.pop()            

        return len(stacks)
    
# @lc code=end

s = "ABFCACDB"
sol = Solution()
ans = sol.minLength(s)
print(ans)
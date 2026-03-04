#
# @lc app=leetcode id=2810 lang=python3
#
# [2810] Faulty Keyboard
#

# @lc code=start
from collections import deque


class Solution:
    def finalString(self, s: str) -> str:
        que = deque()        
        backward = True

        for c in s:
            if c == 'i':
                backward = not backward
            else:
                if backward:
                    que.append(c)
                else:
                    que.appendleft(c)

        if not backward:
            que = reversed(que)
                
        return ''.join(que)
        
# @lc code=end

s = "string"
sol = Solution()
ans = sol.finalString(s)
print(ans)

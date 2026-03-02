#
# @lc app=leetcode id=3412 lang=python3
#
# [3412] Find Mirror Score of a String
#

# @lc code=start
from collections import defaultdict


class Solution:          
    def calculateScore(self, s: str) -> int:
        chars = [chr(o) for o in range(ord('a'), ord('z')+1)]

        d = defaultdict(list)
        ans = 0

        for i, c in enumerate(s):
            if len(d[c]) > 0:
                ans += i - d[c].pop()
            
            else: 
                mirraor = chars[(ord(c)-ord('a')+1) * -1]
                d[mirraor].append(i)
                        
        return ans
# @lc code=end

s = "aczzx"

sol = Solution()
ans = sol.calculateScore(s)
print(ans)



#
# @lc app=leetcode id=3597 lang=python3
#
# [3597] Partition String 
#

# @lc code=start
from typing import List


class Solution1:
    def partitionString(self, s: str) -> List[str]:
        ans = []
        dup = set()
        t = ''
        for c in s:
            t += c
            if t not in dup:
                ans.append(t)
                dup.add(t)
                t = ''
            
        return ans

class Solution:
    def partitionString(self, s: str) -> List[str]:
        cur = root = {}

        ans = []
        t = ''
        for c in s:
            t += c
            if c not in cur:
                ans.append(t)
                t = ''
                cur[c] = {}
                cur = root
            else:
                cur = cur[c]
        
        return ans
                




# @lc code=end

s = "abbccccd"

sol = Solution()
ans = sol.partitionString(s)
print(ans)

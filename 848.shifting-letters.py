#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
from typing import List


class Solution:
    def shift(self, c, k):
        n = (ord(c) - ord('a') + k) % 26
        res = chr(ord('a') + n)        
        return res

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = []
        l = len(s)
        count = 0
        
        for i in range(l-1, -1, -1):
            count += shifts[i]            
            c = self.shift(s[i], count)
            res.append(c)
            
        res = ('').join(res[::-1])
        return res
        
# @lc code=end


s = "abc"
shifts = [3,5,9]

sol = Solution()
ans = sol.shiftingLetters(s, shifts)
print(ans)

# print(sol.shift('a', 3))


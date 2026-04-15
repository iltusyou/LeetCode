#
# @lc app=leetcode id=1332 lang=python3
#
# [1332] Remove Palindromic Subsequences
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s) 

        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return 2
            
        return 1
# @lc code=end

s = "ababa"

sol = Solution()
ans = sol.removePalindromeSub(s)
print(ans)
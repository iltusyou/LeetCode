#
# @lc app=leetcode id=3360 lang=python3
#
# [3360] Stone Removal Game
#

# @lc code=start
class Solution:
    def canAliceWin(self, n: int, take: int = 10) -> bool:
        return n >= take and not self.canAliceWin(n-take, take-1)
        
# @lc code=end




sol = Solution()

# for n in range(1, 51):
#     ans = sol.canAliceWin(n)
#     print(n, ans)


sol.canAliceWin(1)
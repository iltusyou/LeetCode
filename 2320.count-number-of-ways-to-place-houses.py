#
# @lc app=leetcode id=2320 lang=python3
#
# [2320] Count Number of Ways to Place Houses
#

# @lc code=start
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 1000000007

        dp = [1, 1]
        for _ in range(n):
            dp.append(dp[-1] + dp[-2])

        ans = dp[-1] * dp[-1]
        ans = ans % MOD

        return ans
# @lc code=end

n = 1
# n = 2

sol = Solution()
ans = sol.countHousePlacements(n)
print(ans)
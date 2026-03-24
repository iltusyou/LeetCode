#
# @lc app=leetcode id=2571 lang=python3
#
# [2571] Minimum Operations to Reduce an Integer to 0
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        b = bin(n)[2:]

        cnt0 = b.count('0')
        cnt1 = len(b) - cnt0


        print(b, cnt0, cnt1)

        return
# @lc code=end

n = 39

sol = Solution()
ans = sol.minOperations(n)
print(ans)
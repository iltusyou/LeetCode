#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        while n >= 5:
            ans += n//5
            n //= 5
        
        return ans
        
# @lc code=end


# n = 3
n = 5
# n = 0
# n = 30

sol = Solution()
ans = sol.trailingZeroes(n)
print(ans)
#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low +=1

        if high % 2 == 0:
            high -= 1

        res = ((high - low) // 2) + 1

        return res
    
# @lc code=end

low = 3
high = 7

# low = 8
# high = 10

sol = Solution()
ans = sol.countOdds(low, high)
print(ans)
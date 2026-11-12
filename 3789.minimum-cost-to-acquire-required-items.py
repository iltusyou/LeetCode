#
# @lc app=leetcode id=3789 lang=python3
#
# [3789] Minimum Cost to Acquire Required Items
#

# @lc code=start
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = 0

        minCostBoth = min(costBoth, cost1 + cost2)
        minNeedBoth = min(need1, need2)

        need1 -= minNeedBoth
        need2 -= minNeedBoth
        ans += minNeedBoth * minCostBoth

        ans += need1 * min(cost1, costBoth)
        ans += need2 * min(cost2, costBoth)

        return ans
# @lc code=end

cost1 = 3
cost2 = 2
costBoth = 1
need1 = 3
need2 = 2

sol = Solution()
ans = sol.minimumCost(cost1, cost2, costBoth, need1, need2)
print(ans)
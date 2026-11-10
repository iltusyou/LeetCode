#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_n = min(nums)
        ans = sum(nums) - min_n * len(nums)

        return ans
    
# @lc code=end

nums = [1,2,3]

sol = Solution()
ans = sol.minMoves(nums)
print(ans)
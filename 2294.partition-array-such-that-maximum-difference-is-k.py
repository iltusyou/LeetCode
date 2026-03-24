#
# @lc app=leetcode id=2294 lang=python3
#
# [2294] Partition Array Such That Maximum Difference Is K
#

# @lc code=start
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        end, ans = -1, 0
        for n in nums:
            if n > end:
                ans += 1
                end = n + k

        return ans
# @lc code=end

nums = [3,6,1,2,5]
k = 2

sol = Solution()
ans = sol.partitionArray(nums, k)
print(ans)



#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        deq = deque()        

        for i, x in enumerate(nums):
            if len(deq) == 0:
                deq.append(x)            
                continue

            







        return
# @lc code=end

nums = [8,2,4,7]
limit = 4

sol = Solution()
ans = sol.longestSubarray(nums, limit)
print(ans)


#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        dup = set()
        for n in nums:
            if n in dup:
                return n
            dup.add(n)

# @lc code=end

nums = [1,2,3,3]
sol = Solution()
ans = sol.repeatedNTimes(nums)
print(ans)
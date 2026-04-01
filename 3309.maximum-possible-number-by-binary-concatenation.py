#
# @lc app=leetcode id=3309 lang=python3
#
# [3309] Maximum Possible Number by Binary Concatenation
#

# @lc code=start
from functools import cmp_to_key
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        bin_nums = [ bin(n)[2:] for n in nums]

        key = cmp_to_key (lambda x, y: int(y+x) - int(x+y))
        sorted_nums = sorted(bin_nums, key = key)
        # print(bin_nums, sorted_nums)

        ans = ''.join(sorted_nums)
        ans = int(ans, 2)

        return ans
# @lc code=end

nums = [1,2,3]

sol = Solution()
ans = sol.maxGoodNumber(nums)
print(ans)
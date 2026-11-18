#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        inc = deque()
        inc.append(nums[0])
        lenInc = 1

        dec = deque()
        dec.append(nums[0])
        lenDec = 1

        for i in range(1, n):
            if nums[i] <= inc[-1]:
                lenInc = max(len(inc), lenInc)
                inc.clear()

            inc.append(nums[i])

            if nums[i] >= dec[-1]:
                lenDec = max(len(dec), lenDec)
                dec.clear()

            dec.append(nums[i])

            # print(inc, dec, lenInc, lenDec)

        lenInc = max(len(inc), lenInc)
        lenDec = max(len(dec), lenDec)
        ans = max(lenInc, lenDec)

        return ans
        
# @lc code=end

# nums = [1,4,3,3,2]
nums = [3,2,1]

sol = Solution()
ans = sol.longestMonotonicSubarray(nums)
print(ans)
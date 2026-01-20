#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        count = 0
        right = - float('inf')
        intervals.sort(key= lambda x:x[1])

        for v in intervals:
            if v[0] >= right:
                right = v[1]
                count += 1

        res = n - count

        return res
    
# @lc code=end

intervals = [[1,2],[2,3],[3,4],[1,3]]
sol = Solution()
ans = sol.eraseOverlapIntervals(intervals)
print(ans)


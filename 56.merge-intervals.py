#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])

        n = len(intervals)        
        res = []
        right = -1

        for i in range(0, n):            

            if intervals[i][0] > right:                
                res.append(intervals[i])
                right = intervals[i][1]
                                                
            else:
                right = max(res[-1][1], intervals[i][1])
                res[-1][1] = right
                
        return res
        
# @lc code=end

intervals = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()
ans = sol.merge(intervals)
print(ans)

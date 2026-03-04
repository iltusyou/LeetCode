#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])        

        h = [intervals[0][1]]                

        for i in range(1, len(intervals)):
            if intervals[i][0] > h[0]:
                heapq.heappop(h)                            
            heapq.heappush(h, intervals[i][1])
        
        return len(h)
# @lc code=end

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
sol = Solution()
ans = sol.minGroups(intervals)



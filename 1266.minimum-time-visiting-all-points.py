#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
from itertools import pairwise
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        ans = 0

        for (x1, y1), (x2, y2) in pairwise(points):

            dx = abs(x2 - x1)
            dy = abs(y2 - y1) 
            z = min(dx, dy) #走斜的            

            ans += dx + dy - z            
            
        return ans
    
# @lc code=end

points = [[1,1],[3,4],[-1,0]]
# points = [[3,2],[-2,2]]

sol = Solution()
ans = sol.minTimeToVisitAllPoints(points)
print(ans)

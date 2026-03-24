#
# @lc app=leetcode id=3111 lang=python3
#
# [3111] Minimum Rectangles to Cover Points
#

# @lc code=start
from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points = sorted(list(set([x for x, _ in points]))) 

        print(points)

        if w == 0:
            return len(points)

        end, ans = -1, 0

        for n in points:
            if n > end:                
                ans += 1
                end = n + w
                print(n, end)
        
        return ans   
# @lc code=end

# points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]
# w = 1

points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
w = 2

sol = Solution()
ans = sol.minRectanglesToCoverPoints(points, w)
print(ans)


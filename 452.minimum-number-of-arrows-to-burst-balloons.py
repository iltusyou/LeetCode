#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0]))
        print(points)    

        count = 0
        minRight = -float('inf')

        for p in points:
            if p[0] > minRight:
                minRight = p[1]
                count += 1

            else:
                minRight = min(minRight, p[1])

            print(p, minRight, count)

        # count = 0
        # inter = [float('inf'), -float('inf')]

        # for p in points:
        #     # 無交集才增加
        #     if p[1] < inter[0] or p[0] > inter[1]:
        #         inter = p
        #         count +=1

        #     else:
        #         inter = [ max(inter[0], p[0]), min(inter[1], p[1]) ]              

        return count
        
# @lc code=end

# points = [[10,16],[2,8],[1,6],[7,12]]
# points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]

sol = Solution()
ans = sol.findMinArrowShots(points)
print(ans)

#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        if n == 2:
            return True
        
        def calM(x1, x2, y1, y2):
            if x2 == x1:
                return float('inf')
            return (y2 - y1) / (x2 - x1)        

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[-1]
        m = calM(x1, x2, y1, y2)
        
        for i in range(1, n):
            x2, y2 = coordinates[i]
            m2 = calM(x1, x2, y1, y2)
            if m != m2:
                return False

        return True
# @lc code=end

# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

coordinates = [[0,0],[0,1],[0,-1]]

sol = Solution()
ans = sol.checkStraightLine(coordinates)
print(ans)
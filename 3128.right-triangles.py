#
# @lc app=leetcode id=3128 lang=python3
#
# [3128] Right Triangles
#

# @lc code=start
from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # print(n, m)

        a = [[0] * m for _ in range(n)]
        for i, row in enumerate(grid):
            s = sum(row)
            
            if s > 1:                
                for j, x in enumerate(row):
                    if x > 0:                        
                        a[i][j] = s-1


        ans = 0   
        b = [[0] * m for _ in range(n)]
        for j in range(m):            
            s = sum([grid[i][j] for i in range(n)])       
            
            if s > 1 and not all(a[i][j] == 0 for i in range(n)):
                for i in range(n):
                    if grid[i][j] > 0:
                       b[i][j] = s-1
                       ans += a[i][j] * b[i][j]


        # print(a)
        # print(b)
        return ans
# @lc code=end
# grid = [[0,1,0],[0,1,1],[0,1,0]]
grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
# grid = [[1,1],[1,1],[1,1]]

sol = Solution()
ans = sol.numberOfRightTriangles(grid)
print(ans)
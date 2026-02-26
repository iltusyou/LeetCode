#
# @lc app=leetcode id=3148 lang=python3
#
# [3148] Maximum Difference Score in a Grid
#

# @lc code=start
from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        score = [[0] * (n) for _ in range(m)]
        path_min = [[float('inf')] * (n) for _ in range(m)]

        res = -float('inf')
                
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                score[i][j] = x - grid[0][0]
                              
                if i == 0 and j == 0:
                    continue

                if j > 0:
                    path_min[i][j] = min(path_min[i][j], path_min[i][j-1], score[i][j-1]) 

                if i > 0:
                    path_min[i][j] = min(path_min[i][j], path_min[i-1][j], score[i-1][j])                    
                
                res = max(res, score[i][j] - path_min[i][j])                             
        
        return res
    
# @lc code=end

# grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
grid = [[4,3,2],[3,2,1]]

sol = Solution()
ans = sol.maxScore(grid)
print(ans)
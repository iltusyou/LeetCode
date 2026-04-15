#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
             
        def dfs(i, j):            
            if grid[i][j] == 0:
                return
                        
            grid[i][j] = 0
            if i > 0:
                dfs(i-1, j)
            if i < m-1:
                dfs(i+1, j)
            if j > 0:
                dfs(i, j-1)
            if j < n - 1:
                dfs(i, j+1)
                                
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    dfs(i, j)
    
        ans = sum(sum(row) for row in grid)
        return ans
        
                  
        
    
# @lc code=end



sol = Solution()

# ans = sol.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
# ans = sol.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])
ans = sol.numEnclaves(grid = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]])

print(ans)



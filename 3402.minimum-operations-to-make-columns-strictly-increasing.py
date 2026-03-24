#
# @lc app=leetcode id=3402 lang=python3
#
# [3402] Minimum Operations to Make Columns Strictly Increasing
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
   
        ans = 0
        
        for i in range(1, m):
            for j in range(n):                
                              
                if grid[i][j] > grid[i-1][j]:
                    continue

                cur = grid[i-1][j] + 1
                                
                ans += cur - grid[i][j]
                grid[i][j] = cur

        print(grid)
      
        return ans                
        
    
# @lc code=end

grid = [[3,2],[1,3],[3,4],[0,1]]

sol = Solution()
ans = sol.minimumOperations(grid)
print(ans)
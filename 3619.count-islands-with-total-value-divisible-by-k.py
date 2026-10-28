#
# @lc app=leetcode id=3619 lang=python3
#
# [3619] Count Islands With Total Value Divisible by K
#

# @lc code=start
from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
       
   
        def isIslans(x, y):
            
            stack = [(x,y)]
            s = grid[x][y]
            grid[x][y] = 0

            while stack:                        
                
                i, j = stack.pop()
                                                                                         
                if i - 1 >= 0 and grid[i-1][j]>0:
                    stack.append((i-1, j))
                    s += grid[i-1][j]     
                    grid[i-1][j] = 0

                if i + 1 < m and grid[i+1][j]>0:
                    stack.append((i+1, j))
                    s += grid[i+1][j]     
                    grid[i+1][j] = 0

                if j - 1 >= 0 and grid[i][j-1]>0:
                    stack.append((i, j-1))
                    s += grid[i][j-1]     
                    grid[i][j-1] = 0

                if j + 1 < n and grid[i][j+1]>0:
                    stack.append((i, j+1))
                    s += grid[i][j+1]     
                    grid[i][j+1] = 0

              
            
            return s


        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    s = isIslans(i, j)
                
                    if s > 0 and s % k == 0:
                       
                        ans += 1    
            
        return ans
    
# @lc code=end

# grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
# k = 5

# grid = [[3,0,3,0],[0,3,0,3],[3,0,3,0]]
# k = 3

# grid = [[16,0],[0,0],[0,0],[0,3],[9,10]]
# k = 13

grid = [[0,0,9,19,0,0],[15,0,9,0,0,0],[0,0,2,1,0,0],[12,0,0,0,0,11],[0,12,0,0,0,0],[12,0,0,0,0,1]]
k = 1

sol = Solution()
ans = sol.countIslands(grid, k)
print(ans)

#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            stack = [(x, y)]
            res = True

            while stack:
                i, j = stack.pop()
                
                if i == 0 or i == m-1:
                    res = False

                if j == 0 or j == n-1:
                    res = False

                if i - 1 >= 0 and grid[i-1][j] == 0:
                    stack.append((i-1, j))                    
                                    
                if i + 1 < m and grid[i+1][j] == 0:
                    stack.append((i+1, j))                    
                                    
                if j - 1 >= 0 and grid[i][j-1] == 0:
                    stack.append((i, j-1))                    
                
                if j + 1 < n and grid[i][j+1] == 0:
                    stack.append((i, j+1))                    

                grid[i][j] = 1

            return res

        ans = 0
        for i in range(m):
            for j in range(n):                                    
                if grid[i][j] == 0:
                    if dfs(i, j):
                        print(i, j)
                        ans += 1

        return ans

            


        
# @lc code=end

# grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
grid = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]

sol = Solution()
ans = sol.closedIsland(grid)
print(ans)
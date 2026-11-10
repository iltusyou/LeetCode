#
# @lc app=leetcode id=3665 lang=python3
#
# [3665] Twisted Mirror Path Count
#

# @lc code=start
from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[0,0] for _ in range(n+1)] for _ in range(m+1)]

        dp[0][1][0] = 1
        dp[1][0][1] = 1

        def move(i, j):
            if grid[i][j] == 1:
                dp[i+1][j][1] = dp[i][j][0]
                dp[i][j+1][0] = dp[i][j][1]                        
            
            else:
                curr = dp[i][j][0] + dp[i][j][1]
                dp[i+1][j][1] = curr
                dp[i][j+1][0] = curr 

        for j in range(1, n):
            move(0, j)

        for i in range(1, m):
            move(i, 0)

        for i in range(1, m):
            for j in range(1, n):
                move(i, j)                              

        MOD = 10**9 + 7
        ans = (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % MOD

        return ans
# @lc code=end

grid = [[0,1,0],[0,0,1],[1,0,0]]

sol = Solution()
ans = sol.uniquePaths(grid)
print(ans)
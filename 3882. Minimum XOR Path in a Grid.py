class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [set() for _ in range(n)]

        dp[0] = {grid[0][0]}

        for j in range(1, n):                        
            dp[j] = { x ^ grid[0][j] for x in dp[j-1] }
    
        for i in range(1, m):
            for j in range(n):
                s = dp[j]

                if j > 0:
                    s.update(dp[j-1])                    
                
                dp[j] = { x ^ grid[i][j] for x in s }
                        
        return min(dp[-1])

        

# grid = [[1,2],[3,4]]
# grid = [[26,24,3],[2,22,17]]
grid = [[19],[5]]

sol = Solution()
ans = sol.minCost(grid)
print(ans)
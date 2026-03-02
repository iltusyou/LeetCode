#
# @lc app=leetcode id=2536 lang=python3
#
# [2536] Increment Submatrices by One
#

# @lc code=start
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n+1) for _ in range(n+1)]
        
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] +=1
            diff[r1][c2+1] -= 1
            diff[r2+1][c1] -= 1
            diff[r2+1][c2+1] += 1

        ans = [[0] * n for _ in range(n)]        
        
        ans[0][0] = diff[0][0]
        
        for j in range(1, n):
            ans[0][j] = diff[0][j] + ans[0][j-1]

        for i in range(1, n):
            ans[i][0] = diff[i][0] + ans[i-1][0]
            
        for i in range(1, n):
            for j in range(1, n):
                ans[i][j] = ans[i-1][j] + ans[i][j-1] - ans[i-1][j-1] + diff[i][j]

        return ans
    
# @lc code=end

# n = 3
# queries = [[1,1,2,2],[0,0,1,1]]

n = 2
queries = [[0,0,1,1]]

sol = Solution()
ans = sol.rangeAddQueries(n, queries)
print(ans)
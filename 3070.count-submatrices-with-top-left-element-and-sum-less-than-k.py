#
# @lc app=leetcode id=3070 lang=python3
#
# [3070] Count Submatrices with Top-Left Element and Sum Less Than k
#

# @lc code=start
from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        s = [[0] * (n+1) for _ in range(m+1)]

        count = 0

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + x
                if s[i+1][j+1] > k:
                    break                
                count+=1
            
        return count
# @lc code=end

# grid = [[7,6,3],[6,6,1]]
# k = 18

# grid = [[7,2,9],[1,5,0],[2,6,6]]
# k = 20

grid = [[1,10],[7,2],[9,1],[4,1]]
k = 8

sol = Solution()
ans = sol.countSubmatrices(grid, k)
print(ans)
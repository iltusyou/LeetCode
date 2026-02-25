#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#

# @lc code=start
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n+1) for _ in range(m+1)]

        for i, row in enumerate(mat):
            for j, x in enumerate(mat[i]):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + x        


        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            r1 = max(0, i-k)
            r2 = min(m-1, i+k)
            for j in range(n):                
                c1 = max(0, j-k)
                c2 = min(n-1, j+k)              

                ans[i][j] = s[r2+1][c2+1] - s[r2+1][c1] - s[r1][c2+1] + s[r1][c1]
            
        return ans
# @lc code=end

# mat = [[1,2,3],[4,5,6],[7,8,9]]
# k = 1

mat = [[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]]
k = 3


sol = Solution()
ans = sol.matrixBlockSum(mat, k)
print(ans)
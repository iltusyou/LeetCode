#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#

# @lc code=start
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for start in range(1, n):
            i, j  = 0, start
            curr = []
            while i<m and j <n:                
                curr.append(mat[i][j])
                i+=1
                j+=1

            curr.sort()

            i, j, cnt  = 0, start, 0
            while i<m and j <n:                
                mat[i][j] = curr[cnt]
                i+=1
                j+=1
                cnt+=1

        for start in range(0, m):
            i, j  = start, 0
            curr = []
            while i<m and j <n:                
                curr.append(mat[i][j])
                i+=1
                j+=1

            curr.sort()
            
            i, j, cnt  = start, 0, 0
            while i<m and j <n:                
                mat[i][j] = curr[cnt]
                i+=1
                j+=1
                cnt+=1                

        return mat
        
# @lc code=end

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
sol = Solution()
ans = sol.diagonalSort(mat)
print(ans)



#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        r = True
        i,j = 0, 0

        res = []

        while i < m and j < n:     
            res.append(mat[i][j])
            
            if r:
                if j == n-1:
                    i+=1
                    r = not r
                elif i == 0:                    
                    j+=1
                    r = not r
                else:
                    i -= 1
                    j += 1

            else:
                if i == m-1:                    
                    j+=1
                    r = not r
                elif j == 0:                    
                    i+=1
                    r = not r
                else:
                    i+=1
                    j-=1
          
        return res
# @lc code=end

# mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[2,5],[8,4],[0,-1]]
sol = Solution()
ans = sol.findDiagonalOrder(mat)
print(ans)
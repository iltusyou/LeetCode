#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#

# @lc code=start
from typing import List


class Solution:
    def isSquare(self, i, j, l, matrix):
            if l == 0:
                return matrix[i][j] == 1
                        
            for r in range(l+1):
                print(i+r, j+1)

                if matrix[i+r][j+l] == 0:
                    return False
                
            for c in range(l+1):
                if matrix[i+l][j+c] == 0:
                    return False            
            
            return True

    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])        

        ans = 0
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                l = 0
                while i + l < m and j + l < n:
                    is_square = self.isSquare(i, j, l, matrix)
                    # print(i, j, l, is_square)
                    if is_square:
                        ans += 1
                        
                    else:
                        break                                       

                    l += 1                
        return ans
# @lc code=end

# matrix = \
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]

matrix =\
[[1,0,1],[1,1,0],[1,1,0]]

sol = Solution()
ans = sol.countSquares(matrix)
print(ans)

# a = sol.isSquare(1,0,1,matrix)
# print(a)
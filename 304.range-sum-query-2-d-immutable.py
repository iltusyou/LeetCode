#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n+1) for _ in range(m+1)]

        for i, row in enumerate(matrix):
            for j, x in enumerate(matrix[i]):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + x

        self.s = s
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.s[row2+1][col2+1] - self.s[row2+1][col1] - self.s[row1][col2+1] + self.s[row1][col1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

input = [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
matrix = input[0][0]

obj = NumMatrix(matrix)

ans = [None]
for i in range(1, len(input)):
    row1 = input[i][0]
    col1 = input[i][1]
    row2 = input[i][2]
    col2 = input[i][3]
    param_1 = obj.sumRegion(row1,col1,row2,col2)
    ans.append(param_1)

print(ans)

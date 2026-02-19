#
# @lc app=leetcode id=3446 lang=python3
#
# [3446] Sort Matrix by Diagonals
#

# @lc code=start
from typing import List


class Solution:        
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(1, n):
            nums = []
            j, k = 0, i
            while j < n and k < n:            
                num = grid[j][k]
                nums.append(num)
                j+=1
                k+=1

            nums.sort(reverse=True)

            j, k = 0, i
            while j < n and k < n:            
                grid[j][k] = nums.pop()
                
                j+=1
                k+=1
        
        for i in range(0, n):
            nums = []
            j, k = i, 0
            while j < n and k < n:
                num = grid[j][k]
                nums.append(num)
                j+=1
                k+=1

        
            nums.sort()

            j, k = i, 0
            while j < n and k < n:            
                grid[j][k] = nums.pop()
                
                j+=1
                k+=1                
        
        return grid
        
# @lc code=end


grid = [[1,7,3],[9,8,2],[4,5,6]]

sol = Solution()
ans = sol.sortMatrix(grid)
print(ans)
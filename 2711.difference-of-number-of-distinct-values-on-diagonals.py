#
# @lc app=leetcode id=2711 lang=python3
#
# [2711] Difference of Number of Distinct Values on Diagonals
#

# @lc code=start
from typing import List

class Solution:
    def calc(self, arr: List[int]) -> tuple:
        n = len(arr)
        if n == 1:
            return [0], [0]

        leftAbove = [0] * n
        rightBelow = [0] * n
        
        leftAboveDiff = set()
        rightBelowDiff = set()

        for i in range(n):                        
            leftAbove[i] = len(leftAboveDiff)
            leftAboveDiff.add(arr[i])

            j = n-1-i
            rightBelow[j] = len(rightBelowDiff)
            rightBelowDiff.add(arr[j])

        return (leftAbove, rightBelow)

    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        for s in range(1, n):
            i, j = 0, s
            curr = []
            while i < m and j < n:
                curr.append(grid[i][j])                
                i+=1
                j+=1

            leftAbove, rightBelow = self.calc(curr)                     

            i, j, cnt = 0, s, 0        
                
            while i < m and j < n:
                grid[i][j] = abs(leftAbove[cnt] - rightBelow[cnt]) 
                i+=1
                j+=1
                cnt+=1


        for s in range(0, m):
            i, j = s, 0
            curr = []
            while i < m and j < n:
                curr.append(grid[i][j])                
                i+=1
                j+=1

            leftAbove, rightBelow = self.calc(curr)

            i, j, cnt = s, 0, 0
            while i < m and j < n:
                grid[i][j] = abs(leftAbove[cnt] - rightBelow[cnt]) 
                i+=1
                j+=1
                cnt+=1
            
        return grid
        
# @lc code=end


grid = [[1,2,3],[3,1,5],[3,2,1]]
sol = Solution()
ans = sol.differenceOfDistinctValues(grid)
print(ans)

# a = sol.calc([2,1,1])
#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from typing import List

# class UnionFind:
#     def __init__(self, m: int, n: int):        
#         self.m = m
#         self.n = n

#         self._fa = [[None for _ in range(n)] for _ in range(m)]
#         self.cc = [[[] for _ in range(n)] for _ in range(m)]

#         # print(self._fa, self.cc)

#     def find(self, t: tuple[int, int]) -> tuple[int, int]|None:
#         x, y = t        

#         if x < 0 or x >= self.m or y < 0 or y >= self.n:
#             return None                

#         fa = self._fa
        
#         if fa[x][y] is None:
#             return None
        
#         if fa[x][y] != (x,y):
#             fa[x][y] = self.find(fa[x][y])

#         return fa[x][y]
    
#     def insert(self, x: int, y: int):        
#         t = (x, y)
#         self._fa[x][y] = t
#         self.cc[x][y].append(t)

#     def merge(self, from_: tuple[int,int], to: tuple[int,int]):        

#         from_ = self.find(from_)
#         to = self.find(to)

#         if from_ is None or to is None or from_ == to:
#             return

#         x_from, y_from = from_
#         x_to, y_to = to

#         self._fa[x_from][y_from] = to

#         self.cc[x_to][y_to].extend(self.cc[x_from][y_from])
#         self.cc[x_from][y_from]=[]
   
#     def get_cc(self):
#         res = []
#         for row in self.cc:
#             for col in row:
#                 res.append(col)

#         res = [c for c in res if len(c) > 0]

#         return res


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        
        done = [[0 for _ in range(n)] for _ in range(m)]


        def dfs(i, j, path):            
            if grid[i][j] == 0 or done[i][j] == 1:
                return
            
            path.append((i, j))
            done[i][j] = 1
            if i > 0:
                dfs(i-1, j, path)
            if i < m-1:
                dfs(i+1, j, path)
            if j > 0:
                dfs(i, j-1, path)
            if j < n - 1:
                dfs(i, j+1, path)
                        
        cc = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                path = []
                dfs(i, j, path)
                if len(path) > 0:
                    cc.append(path)

        print(cc)
                  
        def not_boundary_cnt(arr):
            for a in arr:
                x, y = a        
                is_boundary = x == 0 or x == m-1 or y == 0 or y == n-1

                if is_boundary:
                    return 0
            return len(arr)

        ans = 0
        for c in cc:
            ans += not_boundary_cnt(c)

        return ans
    
# @lc code=end



sol = Solution()

# ans = sol.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
# ans = sol.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])
ans = sol.numEnclaves(grid = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]])

print(ans)



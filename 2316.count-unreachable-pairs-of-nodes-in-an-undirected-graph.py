#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#

# @lc code=start
from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n: int):   
        self._fa = list(range(n))
        self.size = [1 for _ in range(n)]
    
    def find(self, x: int) -> int:
        fa = self._fa
        if fa[x] != x:
            fa[x] = self.find(fa[x])
        return fa[x]
    
    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:
            return False
        
        self._fa[x] = y
        self.size[y] += self.size[x]
        self.size[x] = 0
        
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return (n * (n-1)) // 2
        
        uf = UnionFind(n)
        for i, j in edges:
            uf.merge(i, j)        

        diff = 0
        for i in uf.size:
            if i <= 1:
                continue
            diff += ( i * (i-1)) // 2           

        tot = (n * (n-1)) // 2
        ans = tot - diff

        return ans
      
    
# @lc code=end

# n = 7
# edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]

# n = 12
# edges = []

# n = 12
# edges = [[2,6],[11,3],[5,4],[9,6]]

n = 16
edges = [[0,15],[1,14],[2,11],[4,3],[5,15],[8,2],[14,12]]

sol = Solution()
ans = sol.countPairs(n, edges)
print(ans)
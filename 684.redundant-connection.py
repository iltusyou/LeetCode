#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self._fa = list(range(n))
        self.cc = n     

    def find(self, x):
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])
        return self._fa[x]
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def merge(self, from_, to):
        x, y = self.find(from_), self.find(to)
        if x == y:
            return
        
        self._fa[x] = y
        self.cc -= 1

        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)+1)
        
        for _, (x, y) in enumerate(edges):
            # 在同一個地方 -> 形成環
            if uf.is_same(x, y):
                return [x, y]
                        
            uf.merge(y, x)            


        
# @lc code=end

# edges = [[1,2],[1,3],[2,3]]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

sol = Solution()
ans = sol.findRedundantConnection(edges)
print(ans)
